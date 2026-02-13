---
name: arxiv-api
description: Skill for interacting with arXiv API
type: skill
language: python
---

# arXiv API Skill

## Purpose
Handles all interactions with the arXiv API, including queries, parsing, and error handling.

## Functions

### query_arxiv(categories, max_results=100, days_back=7)
Query arXiv API for papers.

**Parameters:**
- categories (list): arXiv categories (e.g., ['cs.AI', 'cs.LG', 'cs.CV', 'cs.NE'])
- max_results (int): Maximum results per category (default 100)
- days_back (int): Days of papers to fetch (default 7)

**Returns:**
- dict: Raw API response (Atom feed XML)

**Error Handling:**
- HTTPError: Log and return None if API unreachable
- Timeout: Retry up to 3 times with exponential backoff
- Rate limiting: Respect 3-second delay between requests

### parse_papers(atom_feed_xml)
Parse Atom feed XML into structured data.

**Parameters:**
- atom_feed_xml (str): Raw XML from arXiv API

**Returns:**
- list: List of paper dicts with extracted fields

**Fields Extracted:**
- id: arXiv ID (e.g., 2402.12345)
- title: Paper title
- authors: List of author names
- published: ISO 8601 timestamp
- abstract: Paper abstract
- pdf_url: Direct PDF link
- categories: List of arXiv categories

### validate_paper(paper_dict)
Validate a single paper entry.

**Parameters:**
- paper_dict (dict): Paper data to validate

**Returns:**
- tuple: (is_valid: bool, errors: list)

**Checks:**
- All required fields present
- No empty strings
- Valid URLs
- Valid ISO 8601 dates

## Usage Example
```python
from arxiv_api import query_arxiv, parse_papers, validate_paper

categories = ['cs.AI', 'cs.LG']
response = query_arxiv(categories, max_results=50, days_back=14)
papers = parse_papers(response)
valid_papers = [p for p in papers if validate_paper(p)[0]]
```

## Constants
- ARXIV_BASE_URL = "http://export.arxiv.org/api/query"
- REQUEST_DELAY = 3  # seconds
- TIMEOUT = 30  # seconds
- RETRIES = 3
