# arXiv Paper Feed Project - Implementation Plan

## Problem Statement
Build a Terminal-based Copilot system that orchestrates a data pipeline to create an auto-updating arXiv paper feed HTML page. The system fetches real-time data from the arXiv API for AI/ML related papers, displays them in a webpage (title, authors, abstract, PDF link), and refreshes automatically every midnight EST via GitHub Actions.

## Architecture Overview
- **Custom Agents** (.github/agents/): Orchestrate data fetching and HTML generation
- **Skills** (.github/skills/): Reusable functions for API calls, data processing, and HTML templating
- **Prompts** (.github/prompts/): Instructions for agent execution
- **GitHub Actions Workflow**: Triggers daily updates at midnight EST
- **Output Files**: 
  - `data/papers.json` - Paper metadata from arXiv API
  - `arxiv-feed.html` - Rendered webpage with papers
  - `scripts/fetch-arxiv.py` - Python utility for API interaction

## Workplan

### Phase 1: Agent Design
- [ ] Create orchestrator agent (`fetch-arxiv.agent.md`) - coordinates the entire pipeline
- [ ] Create data-fetcher agent (`data-fetcher.agent.md`) - interacts with arXiv API
- [ ] Create page-generator agent (`page-generator.agent.md`) - generates HTML output
- [ ] Create code-quality agent (`code-quality.agent.md`) - validates and enforces code standards

### Phase 2: Skills Development
- [ ] Create arXiv API skill (`arxiv-api.skill.md`) - handles API requests and parsing
- [ ] Create data processor skill (`data-processor.skill.md`) - cleans and transforms paper data
- [ ] Create HTML generator skill (`html-generator.skill.md`) - creates HTML from JSON data
- [ ] Create file operations skill (`file-ops.skill.md`) - handles JSON and file I/O
- [ ] Create code validation skill (`code-validator.skill.md`) - linting and syntax checking
- [ ] Create style formatter skill (`style-formatter.skill.md`) - auto-formats code to standards

### Phase 3: Prompts & Instructions
- [ ] Create orchestrator prompt (`orchestrator.prompt.md`) - pipeline workflow
- [ ] Create fetcher prompt (`fetcher.prompt.md`) - arXiv search instructions
- [ ] Create generator prompt (`generator.prompt.md`) - HTML generation guidelines
- [ ] Create coding standards prompt (`coding-standards.prompt.md`) - style guide and HTML conventions
- [ ] Create code-quality prompt (`code-quality.prompt.md`) - validation and linting rules

### Phase 4: GitHub Actions Workflow
- [ ] Create update-arxiv.yml workflow file - triggers at midnight EST

### Phase 5: Scripts & Utilities
- [ ] Create fetch-arxiv.py - Python utility for arXiv API interaction
- [ ] Create initial data/papers.json structure

### Phase 6: HTML & Output
- [ ] Create arxiv-feed.html template/initial structure
- [ ] Ensure responsive design and accessibility

## Key Design Decisions

### Search Categories for arXiv
- **Physics**: astro-ph, cond-mat, gr-qc, hep-ex, hep-ph, nucl-th, quant-ph
- **Mathematics**: math
- **Computer Science**: cs
- **Quantitative Biology**: q-bio
- **Quantitative Finance**: q-fin
- **Statistics**: stat
- **Electrical Engineering**: eess
- **Economics**: econ
- Timeframe: Papers from the last 7 days

### Agent Responsibilities
1. **Orchestrator Agent**: Manages workflow, error handling, and coordination
2. **Data Fetcher Agent**: Calls arXiv API, validates responses, extracts relevant papers
3. **Page Generator Agent**: Transforms JSON data into styled HTML
4. **Code Quality Agent**: Runs validation checks, enforces standards, and reports issues on all generated code

### Skill Architecture
- Skills are Python-based utilities called by agents
- Each skill has a clear input/output contract
- Skills handle error handling and validation

### GitHub Actions Workflow
- Trigger: 0 AM EST (midnight in New York)
- Runs agent pipeline in sequence
- Commits updated papers.json to repository
- Updates arxiv-feed.html file

## Technical Specifications

### arXiv API Integration
- Endpoint: `http://export.arxiv.org/api/query`
- Search categories: cat:cs.AI, cat:cs.LG, cat:cs.CV, cat:cs.NE
- Max results per query: 50-100 papers
- Response format: Atom feed (XML)

### Data Structure (papers.json)
```json
{
  "last_updated": "2026-02-13T19:00:00Z",
  "papers": [
    {
      "id": "2402.xxxxx",
      "title": "...",
      "authors": [...],
      "published": "...",
      "abstract": "...",
      "pdf_url": "...",
      "categories": [...]
    }
  ]
}
```

### HTML Page Structure
- Responsive design (mobile-friendly)
- Search/filter functionality
- Sort by date, relevance
- Copy PDF link button
- Last updated timestamp
- Dark mode support

## Design & Styling - Futuristic Starship Theme

### Visual Theme
- **Background**: Deep space with animated starfield (twinkling stars, subtle parallax)
- **Color Palette**: 
  - Primary: Deep navy/black (#0a0e27, #0f1419)
  - Accent: Neon cyan (#00d9ff) and electric purple (#c21e8d)
  - Text: Light gray (#e0e0e0) with bright white highlights
  - Success/Active: Neon green (#00ff41)

### Starship Paper Cards
Each paper is represented as a "starship" with:
- **Card Structure**: Hexagonal or sleek angular borders (futuristic design)
- **Glowing Effect**: Neon glow around card edges (box-shadow with cyan/purple)
- **Title Section**: Large, bold title as "starship name" with tech-style font (monospace or futura)
- **Authors Section**: Listed as "crew members" in smaller text with icons
- **Abstract Section**: "Mission briefing" - expandable/collapsible for scanlines effect
- **Metadata**: Published date as "launch date", category as "classification"
- **CTA Buttons**: 
  - "Download Manifest" (PDF link) - styled as tech button with hover glow
  - Share/Copy link - styled as control panel button

### Animated Elements
- Starfield background: Particles twinkling at varying opacity and speeds
- **Starship Loading Animation**: As papers load, cards fly away from center/cluster with trajectory animation
  - Direction: Papers move outward in different directions (radial expansion)
  - Duration: ~1.5-2 seconds per card with staggered delays
  - Visual Effect: Trail effect (fading glow tail) as starship flies away
  - End State: Cards settle into final grid position with gentle pulse
  - Alternative: Papers could "warp jump" away with a brief light streak effect
- Hover effects: Cards expand/glow, scanlines appear on text
- Paper counter: Animated digit flip showing total papers loaded
- Last updated: Pulsing indicator showing sync status

### Typography
- **Headings**: `Courier New`, `Roboto Mono`, or similar monospace (futuristic tech look)
- **Body**: `Inter`, `Roboto` for readability
- **Accent**: ALL CAPS for interactive elements, mixed case for content

### Layout
- **Hero Section**: Title "ARXIV STARSHIP FLEET" with large glowing background
- **Control Panel**: Search/filter bar styled as command console
- **Main Grid**: Papers in 1-2 column responsive layout
- **Footer**: Minimalist footer with last sync time and link to arXiv

### Interactive Features
- **Search Glow**: Input field glows on focus with cyan border
- **Filter Tags**: Category filters styled as clickable control buttons
- **Sort Controls**: Dropdown menu with sci-fi styling
- **Loading State**: Animated loading spinner (spinning starship or orbital animation)

## File Structure to Create
```
.github/
├── agents/
│   ├── fetch-arxiv.agent.md
│   ├── data-fetcher.agent.md
│   ├── page-generator.agent.md
│   └── code-quality.agent.md
├── skills/
│   ├── arxiv-api.skill.md
│   ├── data-processor.skill.md
│   ├── html-generator.skill.md
│   ├── file-ops.skill.md
│   ├── code-validator.skill.md
│   └── style-formatter.skill.md
├── prompts/
│   ├── orchestrator.prompt.md
│   ├── fetcher.prompt.md
│   ├── generator.prompt.md
│   ├── coding-standards.prompt.md
│   └── code-quality.prompt.md
└── workflows/
    └── update-arxiv.yml
data/
└── papers.json
scripts/
└── fetch-arxiv.py
└── arxiv-feed.html
```

## Notes & Considerations
- Agent file format: `<name>.agent.md` with YAML frontmatter (per VS Code Copilot docs)
- All agents use Claude model for consistency
- Skills are called via Copilot CLI from agents
- GitHub Actions workflow uses same agents to maintain consistency
- Error handling: Graceful degradation if API fails (keeps last known state)
- Rate limiting: arXiv API allows ~1 request per 3 seconds
- **Code Quality Agent**: Runs as final validation step in pipeline, blocks commits if standards not met
  - Validates: Python syntax, HTML validity, JSON structure, CSS conventions
  - Checks: Naming conventions, indentation, line length, documentation
  - Reports: Issues with specific file locations and fixes
