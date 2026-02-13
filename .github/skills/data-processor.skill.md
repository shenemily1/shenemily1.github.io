---
name: data-processor
description: Skill for processing and transforming paper data
type: skill
language: python
---

# Data Processor Skill

## Purpose
Cleans, validates, and transforms raw arXiv data into the standardized papers.json format.

## Functions

### deduplicate_papers(papers)
Remove duplicate papers from list.

**Parameters:**
- papers (list): List of paper dicts

**Returns:**
- list: Deduplicated paper list (by arXiv ID)

### sort_papers(papers, sort_by='published', order='desc')
Sort papers by various criteria.

**Parameters:**
- papers (list): Paper list to sort
- sort_by (str): Field to sort by ('published', 'title', or 'authors')
- order (str): 'asc' or 'desc'

**Returns:**
- list: Sorted paper list

### filter_papers(papers, category=None, keyword=None)
Filter papers by category or keyword.

**Parameters:**
- papers (list): Paper list to filter
- category (str): Optional category filter
- keyword (str): Optional keyword to search in title/abstract

**Returns:**
- list: Filtered paper list

### add_metadata(papers, last_updated=None)
Add metadata to papers list.

**Parameters:**
- papers (list): Paper list
- last_updated (str): ISO 8601 timestamp (default: current time)

**Returns:**
- dict: Papers with metadata wrapper

**Output Structure:**
```json
{
  "last_updated": "2026-02-13T19:00:00Z",
  "total_papers": 42,
  "categories": ["cs.AI", "cs.LG"],
  "papers": [...]
}
```

### truncate_abstract(abstract, max_length=500)
Truncate abstract for readability.

**Parameters:**
- abstract (str): Full abstract text
- max_length (int): Maximum characters (default 500)

**Returns:**
- str: Truncated abstract with ellipsis if needed

### normalize_authors(authors)
Clean and normalize author list.

**Parameters:**
- authors (list): Raw author list

**Returns:**
- list: Cleaned author names (title case, no XML tags)

## Usage Example
```python
from data_processor import deduplicate_papers, sort_papers, add_metadata

papers = raw_papers  # from arxiv-api skill
papers = deduplicate_papers(papers)
papers = sort_papers(papers, sort_by='published', order='desc')
output = add_metadata(papers[:100], last_updated='2026-02-13T19:00:00Z')
```
