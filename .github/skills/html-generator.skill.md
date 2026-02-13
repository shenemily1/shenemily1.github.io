---
name: html-generator
description: Skill for generating the futuristic HTML starship page
type: skill
language: html-css-javascript
---

# HTML Generator Skill

## Purpose
Transforms papers.json into a visually stunning, interactive HTML starship feed page.

## Components

### HTML Structure
- Semantic HTML5 with proper sections
- Accessibility features (ARIA labels, semantic tags)
- Mobile-first responsive design

### CSS Styling

#### Color Palette
```css
--primary-bg: #0a0e27;      /* Deep navy/black */
--secondary-bg: #0f1419;    /* Slightly lighter */
--accent-cyan: #00d9ff;     /* Neon cyan */
--accent-purple: #c21e8d;   /* Electric purple */
--text-light: #e0e0e0;      /* Light gray */
--text-bright: #ffffff;     /* Bright white */
--success-green: #00ff41;   /* Neon green */
```

#### Typography
- Headings: Courier New, Roboto Mono (monospace, tech look)
- Body: Inter, Roboto (sans-serif, readable)
- Special text: ALL CAPS for UI elements

### Components

#### Hero Section
- "ARXIV STARSHIP FLEET" title with glow effect
- Subtitle with sync status
- Last updated timestamp

#### Control Panel
- Search input (glows on focus, cyan border)
- Category filter buttons
- Sort dropdown
- Loading spinner

#### Starship Cards
Each paper is styled as a starship:
- Hexagonal/angular borders
- Neon glow effects (box-shadow)
- Title (starship name) in monospace
- Authors (crew members) with icons
- Abstract (mission briefing) - collapsible
- Launch date
- Classification (categories)
- "Download Manifest" button (PDF link)
- Share/Copy button

#### Animations
- Starfield: Twinkling stars background (CSS animation)
- Loading: Cards fly outward from center with trails (~1.5-2s, staggered)
- Hover: Card expansion, glow intensify, scanlines appear
- Counter: Digit flip animation for paper count
- Sync: Pulsing indicator

#### Footer
- Last sync timestamp
- Link to arXiv
- Project credit

### JavaScript Functions

#### loadPapers(jsonPath)
Load papers.json and render cards.

#### renderCard(paper)
Create HTML for single starship card.

#### filterPapers(category, keyword)
Filter displayed cards client-side.

#### sortPapers(sortBy, order)
Sort displayed cards.

#### animateCardEntry(card, index)
Trigger flying-in animation with delay.

#### toggleAbstract(cardId)
Expand/collapse mission briefing.

### Responsive Breakpoints
- Mobile: < 768px (1 column)
- Tablet: 768px - 1024px (1.5 columns)
- Desktop: > 1024px (2 columns)

## Output
Single arxiv-feed.html file with:
- Inline CSS (no external dependencies preferred)
- Self-contained JavaScript
- Fallback for JS disabled
- Valid HTML5
