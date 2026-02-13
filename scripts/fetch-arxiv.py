#!/usr/bin/env python3
"""
Fetch latest arXiv papers for AI/ML research.

This script queries the arXiv API for recent papers in AI, ML, Computer Vision,
and Neural Networks, then stores the results in JSON format.

Author: arXiv Starship Fleet
Date: 2026-02-13
"""

import json
import logging
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from xml.etree import ElementTree as ET

import requests

# Configuration
ARXIV_BASE_URL = "http://export.arxiv.org/api/query"
# Broad arXiv category codes covering multiple disciplines
CATEGORIES = [
    "astro-ph",  # Astrophysics
    "cond-mat",  # Condensed Matter
    "gr-qc",     # General Relativity and Quantum Cosmology
    "hep-ex",    # High Energy Physics - Experiment
    "hep-ph",    # High Energy Physics - Phenomenology
    "nucl-th",   # Nuclear Theory
    "quant-ph",  # Quantum Physics
    "math",      # Mathematics (all subcategories)
    "cs",        # Computer Science (all subcategories)
    "q-bio",     # Quantitative Biology
    "q-fin",     # Quantitative Finance
    "stat",      # Statistics
    "eess",      # Electrical Engineering and Systems Science
    "econ"       # Economics
]
MAX_RESULTS_PER_CATEGORY = 50
DAYS_BACK = 7
REQUEST_DELAY = 3  # seconds between requests
TIMEOUT = 30  # seconds
RETRIES = 3
OUTPUT_DIR = Path(__file__).parent.parent / "data"
OUTPUT_FILE = OUTPUT_DIR / "papers.json"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def query_arxiv(
    category: str,
    max_results: int = MAX_RESULTS_PER_CATEGORY,
    days_back: int = DAYS_BACK
) -> Optional[str]:
    """
    Query arXiv API for papers in a given category.

    Args:
        category: arXiv category code (e.g., 'cs', 'math', 'astro-ph')
        max_results: Maximum number of results (default 50)
        days_back: Number of days of recent papers (default 7)

    Returns:
        Raw XML response as string, or None if request fails

    Raises:
        requests.exceptions.Timeout: If request times out
    """
    # Build search query - simpler approach: just use category, sort by date
    # The API will return recent papers by default when sorted by submittedDate
    query = f"cat:{category}"

    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }

    for attempt in range(RETRIES):
        try:
            logger.info(f"Fetching {category} (attempt {attempt + 1}/{RETRIES})")
            response = requests.get(
                ARXIV_BASE_URL,
                params=params,
                timeout=TIMEOUT
            )
            response.raise_for_status()
            return response.text

        except requests.exceptions.Timeout:
            logger.warning(f"Timeout on {category}, attempt {attempt + 1}")
            if attempt < RETRIES - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                logger.error(f"Failed to fetch {category} after {RETRIES} retries")
                return None

        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {category}: {e}")
            return None


def parse_papers(xml_content: str) -> List[Dict]:
    """
    Parse arXiv Atom feed XML response.

    Args:
        xml_content: Raw XML response from arXiv API

    Returns:
        List of paper dictionaries with extracted metadata
    """
    papers = []

    try:
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        logger.error(f"Failed to parse XML: {e}")
        return papers

    # Define namespaces
    namespaces = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom"
    }

    # Extract entries
    for entry in root.findall("atom:entry", namespaces):
        try:
            paper = _extract_paper(entry, namespaces)
            if paper:
                papers.append(paper)
        except Exception as e:
            logger.warning(f"Failed to parse entry: {e}")
            continue

    logger.info(f"Parsed {len(papers)} papers from XML")
    return papers


def _extract_paper(entry: ET.Element, namespaces: Dict[str, str]) -> Optional[Dict]:
    """
    Extract paper metadata from XML entry.

    Args:
        entry: XML element representing a paper
        namespaces: XML namespaces dictionary

    Returns:
        Dictionary with paper metadata, or None if invalid
    """
    # Extract fields
    title_elem = entry.find("atom:title", namespaces)
    title = title_elem.text.strip() if title_elem is not None else None

    published_elem = entry.find("atom:published", namespaces)
    published = published_elem.text if published_elem is not None else None

    summary_elem = entry.find("atom:summary", namespaces)
    abstract = summary_elem.text.strip() if summary_elem is not None else ""

    # Extract arXiv ID
    arxiv_id = None
    id_elem = entry.find("atom:id", namespaces)
    if id_elem is not None:
        arxiv_id = id_elem.text.split("/abs/")[-1]

    # Extract authors
    authors = []
    for author in entry.findall("atom:author", namespaces):
        name_elem = author.find("atom:name", namespaces)
        if name_elem is not None:
            authors.append(name_elem.text)

    # Extract categories
    categories = []
    for term in entry.findall("atom:category", namespaces):
        term_attr = term.get("term")
        if term_attr:
            categories.append(term_attr)

    # Extract PDF URL
    pdf_url = None
    for link in entry.findall("atom:link", namespaces):
        if link.get("type") == "application/pdf":
            pdf_url = link.get("href")
            break

    # Validate required fields
    if not all([title, published, arxiv_id, authors, abstract]):
        logger.debug(f"Skipping entry with missing fields: {arxiv_id}")
        return None

    return {
        "id": arxiv_id,
        "title": title,
        "authors": authors,
        "published": published,
        "abstract": abstract,
        "pdf_url": pdf_url or f"https://arxiv.org/pdf/{arxiv_id}.pdf",
        "categories": categories
    }


def deduplicate_papers(papers: List[Dict]) -> List[Dict]:
    """
    Remove duplicate papers by arXiv ID.

    Args:
        papers: List of paper dictionaries

    Returns:
        List of unique papers
    """
    seen = set()
    unique = []

    for paper in papers:
        if paper["id"] not in seen:
            seen.add(paper["id"])
            unique.append(paper)

    logger.info(f"Deduplicated: {len(papers)} -> {len(unique)} papers")
    return unique


def add_metadata(papers: List[Dict]) -> Dict:
    """
    Wrap papers with metadata.

    Args:
        papers: List of paper dictionaries

    Returns:
        Dictionary with papers and metadata
    """
    # Use EST timezone for timestamp
    est = timezone(timedelta(hours=-5))
    now = datetime.now(est)

    return {
        "last_updated": now.isoformat(),
        "total_papers": len(papers),
        "categories": CATEGORIES,
        "papers": papers
    }


def save_papers(data: Dict) -> bool:
    """
    Save papers data to JSON file.

    Args:
        data: Dictionary with papers and metadata

    Returns:
        True if successful, False otherwise
    """
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Backup existing file
        if OUTPUT_FILE.exists():
            backup_file = OUTPUT_FILE.with_suffix(".backup.json")
            OUTPUT_FILE.rename(backup_file)
            logger.info(f"Backed up existing file to {backup_file}")

        # Write new file
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logger.info(f"Saved {data['total_papers']} papers to {OUTPUT_FILE}")
        return True

    except IOError as e:
        logger.error(f"Failed to save papers: {e}")
        return False


def main():
    """Main execution function."""
    logger.info("Starting arXiv paper fetch")
    logger.info(f"Categories: {', '.join(CATEGORIES)}")
    logger.info(f"Fetching papers from last {DAYS_BACK} days")

    all_papers = []

    # Fetch papers from each category
    for i, category in enumerate(CATEGORIES):
        if i > 0:
            logger.info(f"Waiting {REQUEST_DELAY} seconds before next request...")
            time.sleep(REQUEST_DELAY)

        xml_response = query_arxiv(category)
        if xml_response:
            papers = parse_papers(xml_response)
            all_papers.extend(papers)
        else:
            logger.warning(f"No response from {category}")

    # Process papers
    logger.info(f"Total papers before deduplication: {len(all_papers)}")
    all_papers = deduplicate_papers(all_papers)

    # Sort by publication date (newest first)
    all_papers.sort(
        key=lambda p: p["published"],
        reverse=True
    )

    # Limit to top 100
    all_papers = all_papers[:100]

    # Add metadata
    output_data = add_metadata(all_papers)

    # Save to file
    if save_papers(output_data):
        logger.info("✓ Successfully completed arXiv fetch")
    else:
        logger.error("✗ Failed to save papers")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
