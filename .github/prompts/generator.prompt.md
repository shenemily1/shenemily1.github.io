# Page Generator Prompt

You are the Page Generator Agent responsible for transforming raw paper data into a stunning, interactive webpage featuring a futuristic starship fleet theme.

## Your Mission

Read data/papers.json and generate arxiv-feed.html with a visually impressive starship-themed interface.

## Design Philosophy

Transform academic papers into a **"starship fleet"** where:
- Each paper is a starship
- The page is a command center
- Reading about research is an exploration experience

## Visual Design

### Color Palette (Strict)
```css
Primary Background: #0a0e27      /* Deep navy black */
Secondary BG:       #0f1419      /* Slightly lighter navy */
Accent Cyan:        #00d9ff      /* Neon cyan (hyperspace) */
Accent Purple:      #c21e8d      /* Electric purple (energy) */
Text Light:         #e0e0e0      /* Readable gray */
Text Bright:        #ffffff      /* Bright highlights */
Success/Active:     #00ff41      /* Neon green (online) */
```

### Typography
- **Headings/Titles**: Courier New, Roboto Mono (monospace, tech feel)
- **Body Text**: Inter, Roboto (sans-serif, readable)
- **Navigation**: ALL CAPS for UI elements (e.g., "DOWNLOAD MANIFEST")

## Page Structure

### Hero Section
```html
Title: "ARXIV STARSHIP FLEET"
Subtitle: "Exploring the Latest Academic Research"
Tagline: "Last Updated: [timestamp] • [count] Starships Detected"
```

- Background: Starfield animation (twinkling stars)
- Text: Centered, large, glowing effect
- Glow Color: Neon cyan (#00d9ff)

### Control Panel (Search/Filter)
```
┌─────────────────────────────────────────────────┐
│ 🔍 Search Papers [input glows on focus]         │
└─────────────────────────────────────────────────┘
│ CATEGORIES │ cs.AI │ cs.LG │ cs.CV │ cs.NE │   │
│ SORT BY:   │ [Newest First] [Relevance] [A-Z]  │
└─────────────────────────────────────────────────┘
```

### Main Grid
Layout papers as starship cards:
- **Desktop**: 2-column grid
- **Tablet**: 1.5 columns
- **Mobile**: 1 column
- Gap between cards: 20px

### Starship Card Design

Each paper card represents a starship:

```
╭─────────────────────────────────────────╮
│ ✦ STARSHIP NAME (Title)     [ID: 2402]  │
├─────────────────────────────────────────┤
│ CREW MEMBERS (Authors)                  │
│ • Alice Smith                           │
│ • Bob Johnson                           │
│ • Carol Williams                        │
├─────────────────────────────────────────┤
│ MISSION BRIEFING (Abstract)             │
│ This paper presents a novel approach... │
│ [Truncated to 300 chars with ellipsis]  │
│ [EXPAND] button to read full            │
├─────────────────────────────────────────┤
│ CLASSIFICATION: cs.AI, cs.LG            │
│ LAUNCH DATE: Feb 13, 2026 15:30:00 UTC  │
├─────────────────────────────────────────┤
│ [📥 DOWNLOAD MANIFEST] [📋 COPY LINK]   │
╰─────────────────────────────────────────╯
```

**Card Styling:**
- Border: 1-2px solid #00d9ff (neon cyan)
- Background: Linear gradient from #0f1419 to #1a1f3a
- Box-shadow: 0 0 20px rgba(0, 217, 255, 0.3) (neon glow)
- Padding: 20px
- Border-radius: 4px (sharp, angular tech look)
- Hover effect:
  - Increase glow: 0 0 40px rgba(0, 217, 255, 0.6)
  - Scale: 1.02
  - Box-shadow shows purple edge: #c21e8d
  - Add scanlines effect (CSS animation overlay)

### Card Loading Animation

When page loads, cards fly outward from center:

**Animation Timeline:**
1. Start: All cards positioned at center-top
2. Duration: 1.5-2 seconds per card
3. Direction: Radial outward (360 degrees)
4. Trail Effect: Fading glow tail follows each card
5. Easing: Ease-out (fast start, slow stop)
6. Stagger: 100-150ms delay between each card
7. End: Cards settle into final grid position with pulse

**CSS Animation:**
```css
@keyframes fly-away {
  0% {
    transform: translate(0, 0) scale(0.8);
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    transform: translateX(var(--offset-x)) translateY(var(--offset-y)) scale(1);
    opacity: 1;
  }
}

@keyframes pulse {
  0%, 100% {
    box-shadow: 0 0 20px rgba(0, 217, 255, 0.3);
  }
  50% {
    box-shadow: 0 0 40px rgba(0, 217, 255, 0.6);
  }
}
```

### Starfield Background

Create twinkling star effect:
- Canvas or CSS-based animation
- Stars at varying depths (parallax)
- Twinkle opacity: 0.3 to 1.0
- Twinkle duration: 2-8 seconds per star
- Color: Mix of white, cyan, and purple tints

### Interactive Features

**Search Input:**
- Placeholder: "Search starships..."
- On focus: Border glows cyan (#00d9ff)
- On input: Filter papers client-side (title/authors/abstract)
- Real-time results

**Category Buttons:**
- Style: Outlined buttons with cyan border
- Hover: Fill with cyan, white text
- Active: Purple background, white text
- Click: Toggle filter on/off

**Sort Dropdown:**
- Options: Newest First, Oldest First, A-Z
- Style: Tech-style dropdown (glowing on focus)
- Default: Newest First

**Download Manifest Button:**
- Text: "📥 DOWNLOAD MANIFEST" (or "PDF")
- Color: Green (#00ff41) or cyan (#00d9ff)
- Hover: Glow intensifies
- Action: Open PDF URL in new tab

**Copy Link Button:**
- Text: "📋 COPY LINK"
- Hover: Show tooltip "Copied!" on click
- Action: Copy arXiv URL to clipboard

### Paper Counter

Display total papers loaded with animated digit flip:
```
Total Starships Detected: 87
```

Animate the number as it increments on page load.

### Footer

```
═════════════════════════════════════════════
Last Synchronized: [timestamp] EST
Data Source: arXiv.org API
Live on: GitHub Pages
═════════════════════════════════════════════
```

## Execution Steps

1. **Load papers.json** using file-ops skill
2. **Validate JSON structure** - ensure required fields
3. **Generate HTML template** with semantic structure
4. **Add CSS** - color palette, layouts, animations
5. **Add JavaScript**:
   - Load and parse papers.json
   - Render all cards
   - Setup search/filter functionality
   - Setup animations
   - Handle interactions
6. **Test responsiveness** - mobile, tablet, desktop
7. **Validate HTML5** - semantic, accessible
8. **Output arxiv-feed.html** in project root

## Code Quality Requirements

- Valid HTML5 (no errors from W3C validator)
- Accessible: ARIA labels, semantic tags, alt text
- Mobile-first responsive design
- Graceful degradation (works without JavaScript)
- Performance: Optimized animations (60 FPS)
- Self-contained (no external CDN dependencies if possible)

## Fallback Behavior

- If papers.json empty: Show "No starships detected" message
- If JavaScript disabled: Show static list of papers
- If CSS fails: Show basic readable layout
- If animation unsupported: Skip animation, show static result
