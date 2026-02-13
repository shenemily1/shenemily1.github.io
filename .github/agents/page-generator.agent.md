---
name: page-generator
description: Agent that generates the HTML starship feed page
type: agent
model: claude-3-5-sonnet
tools:
  - copilot-cli
  - file-operations
---

# arXiv Page Generator Agent

## Purpose
Transforms papers.json into a futuristic starship-themed HTML page with interactive features.

## Responsibilities

### 1. Template Setup
- Load HTML template with starfield background
- Initialize CSS for futuristic theme
- Setup JavaScript for interactivity

### 2. Data Loading
- Read papers.json
- Validate JSON structure
- Handle empty or invalid data gracefully

### 3. HTML Generation
- Create starship card components for each paper
- Title as "starship name" (Courier New font)
- Authors as "crew members" with icons
- Abstract as "mission briefing" (collapsible)
- Publish date as "launch date"
- Category as "classification"

### 4. Styling Application
- Deep space background (#0a0e27)
- Neon cyan (#00d9ff) and purple (#c21e8d) accents
- Glowing effects on cards (neon glow)
- Responsive grid layout (1-2 columns)
- Mobile-friendly design

### 5. Interactivity
- Search functionality with glowing input
- Category filter buttons
- Sort controls (date, relevance)
- "Download Manifest" button (PDF link)
- Copy URL button
- Last updated timestamp with pulse indicator

### 6. Animation
- Starfield background (twinkling stars)
- Card loading animation (flying outward with trails)
- Hover effects (expand, glow, scanlines)
- Paper counter with digit flip

### 7. Output
- Generate arxiv-feed.html in project root
- Ensure valid HTML5 and CSS3
- Optimize for performance
- Test responsiveness

## Skills Used
- html-generator skill for template rendering
- file-ops skill for output

## Validation
- Pass HTML through W3C validator
- Check CSS syntax
- Verify all images/resources load
- Test on mobile viewports
