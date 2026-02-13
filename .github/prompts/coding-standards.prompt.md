# Coding Standards Prompt

## General Code Style Guidelines

All code generated in this project must adhere to these standards.

### Python (scripts/fetch-arxiv.py)

**Indentation & Whitespace**
- Use 4 spaces for indentation (never tabs)
- Max line length: 100 characters (80 for code itself)
- Two blank lines between functions
- Two blank lines between classes
- One blank line between methods

**Naming Conventions**
- Variables: `snake_case` (e.g., `paper_data`, `author_list`)
- Functions: `snake_case` (e.g., `fetch_papers()`, `validate_entry()`)
- Classes: `PascalCase` (e.g., `PaperFetcher`, `DataProcessor`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `API_TIMEOUT = 30`)
- Private: Prefix with `_` (e.g., `_internal_helper()`)

**Documentation**
- All functions must have docstrings (Google style)
- All classes must have docstrings
- Complex logic needs inline comments (but code should be self-documenting)
- No redundant comments

**Example Function:**
```python
def fetch_papers(categories: list, max_results: int = 100, days_back: int = 7) -> list:
    """Fetch papers from arXiv API for given categories.
    
    Args:
        categories: List of arXiv category codes (e.g., ['cs.AI', 'cs.LG'])
        max_results: Maximum papers per category (default 100)
        days_back: Days of recent papers to fetch (default 7)
    
    Returns:
        List of paper dictionaries with metadata
    
    Raises:
        requests.exceptions.Timeout: If API request times out
        ValueError: If categories is empty
    """
```

**Imports**
- Group: stdlib, third-party, local (in that order)
- Alphabetize within groups
- One import per line (except multiple from same module)

```python
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional

import requests
from lxml import etree

from ..skills import arxiv_api
```

**Error Handling**
- Catch specific exceptions, not bare `except`
- Log exceptions with traceback
- Provide meaningful error messages
- Use context managers (`with` statements)

### HTML (arxiv-feed.html)

**Indentation & Structure**
- Use 2 spaces for indentation (never tabs)
- One element per line (generally)
- Logical grouping with blank lines between sections
- Max line length: 120 characters

**Semantic Markup**
- Use semantic HTML5: `<header>`, `<main>`, `<section>`, `<article>`, `<footer>`
- Use `<button>` for buttons (not `<div>` or `<a>`)
- Use `<nav>` for navigation
- Use `<form>` with proper `<input>` elements

**Naming Conventions**
- IDs: `kebab-case` (e.g., `id="paper-card-2402"`)
- Classes: `kebab-case` (e.g., `class="starship-card"`)
- Data attributes: `data-kebab-case` (e.g., `data-paper-id="2402.12345"`)

**Attributes**
- Always quote attribute values
- Order attributes: id, class, data-*, then others
- Accessibility attributes: `role`, `aria-label`, `aria-expanded`

**Accessibility**
- All images need `alt` text
- Interactive elements need labels
- Use semantic HTML (not divs for everything)
- Proper heading hierarchy (h1 once, then h2, h3, etc.)
- ARIA labels for complex interactions

**Example:**
```html
<article class="starship-card" id="paper-2402-12345" data-paper-id="2402.12345">
  <header>
    <h2 class="paper-title">Revolutionary Deep Learning Approach</h2>
    <span class="paper-id" aria-label="arXiv ID">2402.12345</span>
  </header>
  
  <section class="crew-members" aria-label="Authors">
    <h3>Crew Members</h3>
    <ul>
      <li>Alice Smith</li>
      <li>Bob Johnson</li>
    </ul>
  </section>
  
  <section class="mission-briefing">
    <h3>Mission Briefing</h3>
    <p>This paper presents a novel approach...</p>
    <button class="expand-btn" aria-expanded="false">EXPAND</button>
  </section>
  
  <footer>
    <span class="launch-date">Feb 13, 2026</span>
    <span class="classification">cs.AI, cs.LG</span>
    <a href="#" class="pdf-link" aria-label="Download PDF">
      📥 DOWNLOAD MANIFEST
    </a>
  </footer>
</article>
```

### CSS (in HTML style tag)

**Indentation & Spacing**
- Use 2 spaces for indentation
- One rule per line
- Blank line between rule sets
- Max line length: 100 characters

**Naming Conventions**
- Classes: `kebab-case` (e.g., `.starship-card`, `.crew-members`)
- IDs: `kebab-case` (e.g., `#hero-section`)
- Variables (CSS custom properties): `--kebab-case` (e.g., `--primary-color`)
- No element selectors (except resets)

**Organization**
1. CSS Custom Properties (variables)
2. Reset/Base styles
3. Layout classes
4. Component classes
5. Utility classes
6. Media queries (at end)

**Example:**
```css
:root {
  --primary-bg: #0a0e27;
  --accent-cyan: #00d9ff;
  --text-light: #e0e0e0;
}

body {
  background-color: var(--primary-bg);
  color: var(--text-light);
  font-family: 'Inter', sans-serif;
  margin: 0;
  padding: 0;
}

.starship-card {
  border: 1px solid var(--accent-cyan);
  background: linear-gradient(135deg, #0f1419, #1a1f3a);
  padding: 20px;
  border-radius: 4px;
  box-shadow: 0 0 20px rgba(0, 217, 255, 0.3);
}

.starship-card:hover {
  box-shadow: 0 0 40px rgba(0, 217, 255, 0.6);
}

@media (max-width: 768px) {
  .starship-card {
    padding: 15px;
  }
}
```

### JavaScript (in HTML script tag)

**Formatting**
- Use 2 spaces for indentation
- Use semicolons
- One statement per line
- Blank lines between logical blocks

**Naming Conventions**
- Variables: `camelCase` (e.g., `paperCount`, `cardElement`)
- Functions: `camelCase` (e.g., `fetchPapers()`, `renderCard()`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_RESULTS = 100`)
- CSS class selectors: Use constants `const CARD_CLASS = 'starship-card'`

**Function Structure**
```javascript
function renderCard(paper) {
  // Brief function description in comment
  const card = document.createElement('article');
  card.className = 'starship-card';
  card.id = `paper-${paper.id}`;
  
  // Set content...
  
  return card;
}
```

### JSON (data/papers.json)

**Formatting**
- Use 2-space indentation
- Alphabetical property ordering within objects
- No trailing commas
- Valid UTF-8

**Structure Example:**
```json
{
  "categories": ["cs.AI", "cs.LG"],
  "last_updated": "2026-02-13T19:00:00-05:00",
  "papers": [
    {
      "abstract": "...",
      "authors": ["Alice Smith", "Bob Johnson"],
      "categories": ["cs.AI", "cs.LG"],
      "id": "2402.12345",
      "pdf_url": "http://arxiv.org/pdf/2402.12345.pdf",
      "published": "2026-02-13T15:30:00Z",
      "title": "..."
    }
  ],
  "total_papers": 87
}
```

## Cross-File Conventions

**File Names**
- Python: `snake_case.py` (e.g., `fetch-arxiv.py` or `fetch_arxiv.py`)
- HTML: `kebab-case.html` (e.g., `arxiv-feed.html`)
- JSON: `kebab-case.json` (e.g., `papers.json`)
- Agent/Skill files: `kebab-case.agent.md`, `kebab-case.skill.md`

**Comments**
- Use `#` for Python
- Use `<!--` for HTML (multiline OK)
- Use `//` for JavaScript
- Use `/* */` for CSS (multiline)
- Explain WHY, not WHAT (code shows what)

**Version Control**
- Keep files readable (not minified)
- Include headers with file purpose
- Reference related files in comments

## Automated Validation

All code will be validated by:
- **Python**: pylint, black formatter
- **HTML**: html5lib, accessibility checker
- **CSS**: stylelint
- **JSON**: jsonschema
- **General**: Line length, indentation, naming conventions

Run validation before committing:
```bash
code-validator scripts/fetch-arxiv.py
code-validator arxiv-feed.html
code-validator data/papers.json
```
