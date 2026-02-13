---
name: fetch-arxiv
description: Orchestrator agent that coordinates the arXiv paper feed pipeline
type: agent
model: claude-3-5-sonnet
tools:
  - copilot-cli
  - file-operations
---

# arXiv Fetch Orchestrator Agent

## Purpose
Orchestrates the entire data pipeline for fetching and displaying arXiv papers as a starship fleet.

## Workflow

1. **Invoke Data Fetcher**: Call the data-fetcher agent to retrieve latest papers from arXiv API
   - Fetch papers from AI/ML categories
   - Validate API responses
   - Handle rate limiting and errors

2. **Invoke Page Generator**: Call the page-generator agent to create HTML output
   - Transform papers.json into HTML
   - Apply starship-themed styling
   - Generate interactive features

3. **Invoke Code Quality**: Call the code-quality agent for validation
   - Validate all generated files
   - Check coding standards
   - Report any issues

4. **Finalize**: Commit changes or report status
   - Update data/papers.json
   - Update arxiv-feed.html
   - Return success/failure status

## Error Handling
- If API fetch fails: Gracefully degrade and use last known state
- If generation fails: Halt pipeline and report issues
- If validation fails: Block commit and report violations

## Output
- `data/papers.json`: Updated paper metadata
- `arxiv-feed.html`: Rendered webpage
- Status report with timestamp
