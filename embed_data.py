#!/usr/bin/env python3
"""Embed papers.json data into arxiv-feed.html"""

import json

# Read papers data
with open('data/papers.json', 'r', encoding='utf-8') as f:
    papers_data = json.load(f)

# Create compact JSON for embedding
papers_json_str = json.dumps(papers_data, separators=(',', ':'))

print(f"Embedding {len(papers_data['papers'])} papers")
print(f"JSON string size: {len(papers_json_str):,} bytes")

# Read the arxiv-feed.html template
with open('arxiv-feed.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find and replace the data loading script
old_script = '''        /**
         * Load and parse papers.json
         */
        async function loadPapers() {
            try {
                // Try to load papers.json
                const response = await fetch('data/papers.json');
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                allPapers = data.papers || [];
                lastUpdatedEl.textContent = data.last_updated || 'Never';
                totalPapersEl.textContent = data.total_papers || 0;
                
                console.log(`Loaded ${allPapers.length} papers`);
                displayPapers();
            } catch (error) {
                console.error('Error loading papers:', error);
                
                // Fallback: try to create some test data or show empty state
                console.log('Failed to load papers.json. Make sure the file exists in the data/ directory.');
                showEmptyState();
            }
        }'''

new_script = f'''        /**
         * Load and parse papers.json
         */
        async function loadPapers() {{
            // Data is embedded directly in this HTML file
            const data = {papers_json_str};
            
            allPapers = data.papers || [];
            lastUpdatedEl.textContent = data.last_updated || 'Never';
            totalPapersEl.textContent = data.total_papers || 0;
            
            console.log(`Loaded ${{allPapers.length}} papers`);
            displayPapers();
        }}'''

# Replace the script
html_content = html_content.replace(old_script, new_script)

# Write the modified HTML
with open('arxiv-feed.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✓ Successfully embedded papers data into arxiv-feed.html")
print(f"File size: {len(html_content):,} bytes")
