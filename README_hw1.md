# Homework 1: Code with AI - Progress Report
**Due Date**: February 13, 2026  
**Late Days Used**: 0

---

## Introduction
The main purpose of this homework is was to:

- Get experience with AI coding
- Learn how to decompose a problem into smaller tasks and find the right tools to solve them with the help of AI
- Improve your prompt engineering skills
- Conduct the coding task you have never learned before with the help of AI
- Learn the agentic programming paradigm

This README documents my progress on Homework 1, including the solutions to each problem, AI tools used, and prompts used.

---

## Problem 1
For this problem, a homepage for a "coding blog" was to be created, with links to a pacman game and a arXiv digest:
- **Homepage**: `index.html` - A professional, responsive coding blog homepage
- **Features**:
  - Header with title and tagline
  - Navigation menu linking to the following problems
  - Hero section with introduction
  - Project cards for each assignment with descriptions
  - Responsive design
  - Futuristic styling with a starry background
  - Expandable layout for future projects

### Files Created
- `index.html` - Main homepage

### Prompts
1. "Create a professional homepage for a coding blog with navigation links to Pac-Man game and arXiv feed"
2. "Make it responsive and expandable for future projects"

### AI Tools Used
- GitHub Copilot - For creation of files

### GitHub Pages
- Enabled GitHub Pages in repository settings
- Selected `main` branch as source
- Site automatically published at: `https://shenemily1.github.io/homework-1-shenemily1/`

---

## Problem 2: Pac-Man (Valentine's Special) 🎮
For this problem, the following was created:
- Classic Pac-Man mechanics (maze, dots, ghosts)
- Valentine's rose power-up
- Heart projectiles to eliminate ghosts
- Game ends when lives are lost
- Page accessible from homepage

### File Created
- `pacman.html` - Game page that can be accessed from the blog page

### AI Tools Used
- GitHub Copilot - For game logic and mechanics
- Claude - For game design consultation

### Prompts
1. Creating the actual game was done with the following prompt:
    - "Create a Pac-man game with the following core features:
        - **Classic Pac-Man Mechanics**: A maze with dots (pellets) for Pac-Man to eat, and ghosts that chase Pac-Man. The game ends when Pac-Man loses all lives. You can decide the maze layout by yourself (classic ok, but maybe even 3D).
        - **Valentine's Power-Up — Rose** 🌹: A rose randomly appears on the maze from time to time. When Pac-Man eats the rose, it enters a powered-up state for a limited duration (e.g., a few seconds), during which Pac-Man **continuously shoots hearts** in its current facing direction.
        - **Heart Projectiles** 💕: The hearts travel across the maze and eliminate any ghost they hit. Once the power-up expires, Pac-Man returns to normal until it picks up another rose."
2. Many other stylistic modifications were included, such as music, colors, etc. For example, music in the game was created through the following prompt to github copilot:
    - "When the game starts, play an upbeat 8-bit song that is in a swing tempo with 3/4 time. Then, when the power up is eaten by pacman, play a faster song. Return to the previous song when the powerup is gone."

---

## Problem 3: Data Scaffolding from Internet - arXiv Feed 📄

### Requirements
- [ ] Display latest arXiv papers
- [ ] Show paper title, authors, abstract, and PDF link
- [ ] Auto-update every midnight via GitHub Actions
- [ ] Include `.github/workflows` directory
- [ ] Link from homepage

## Steps used to Prompt Copilot CLI
1. Asked Copilot CLI to plan the workflow and file structure for the arXiv feed, using the plan.prompt.md prompt I wrote beforehand
2. Asked Copilot CLI to add a code checker agent, and to update the plan with stylistic choices
3. Prompt Copilot CLI to implement the plan after checking 
4. Prompt Copilot CLI to create the GitHub Actions workflow for daily updates
5. Prompt Copilot CLI to add a link from the homepage to the arXiv feed page

### Files created
- `arxiv-feed.html` - Frontend for displaying papers
- `.github/workflows/update-arxiv.yml` - GitHub Actions workflow
- `scripts/fetch-arxiv.py` - Python script to fetch papers
- `data/papers.json` - Generated paper data
- `embed_data.py` - embed JSON data into the webpage

### AI Tools Used
- Copilot CLI - Primary tool for scaffolding and automation
- GitHub Copilot - Code generation

### Key APIs & Resources
- [arXiv API](https://arxiv.org/help/api/user-manual) - For fetching papers
- [GitHub Actions](https://docs.github.com/en/actions) - For automation

---

## Report

### Tools Used
- **GitHub Copilot**: Code completion, HTML/CSS generation, JavaScript suggestions
- **Claude (Claude Haiku 4.5)**: Design guidance, architecture planning, prompt engineering

### Lessons Learned
1. Breaking problems into smaller tasks makes AI assistance more effective
2. Specific prompts yield better results than vague requests
3. Iterative refinement with AI feedback improves code quality
4. AI excels at generating boilerplate and structure

### Prompt Engineering 
- Be specific about requirements and constraints
- Ask for responsive/accessible design upfront
- Request expandable/modular code structure
- Provide context about use case and audience

### Repository Structure

```
homework-1-shenemily1/
├── README.md (original assignment)
├── README_hw1.md (this progress report)
├── index.html (homepage) ✅
├── pacman.html (game page) [To do]
├── arxiv-feed.html (paper feed page) [To do]
├── css/
│   └── style.css (optional, for shared styles)
├── js/
│   ├── pacman-game.js (game logic) [To do]
│   └── arxiv-display.js (paper display) [To do]
├── scripts/
│   └── fetch-arxiv.py (arXiv API script) [To do]
├── data/
│   └── papers.json (generated paper list) [To do]
└── .github/
    └── workflows/
        └── update-arxiv.yml (automation) [To do]
```
---

## Conclusion
Homework was completed by Emily Shen with the assisstance of AI.