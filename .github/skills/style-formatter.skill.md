---
name: style-formatter
description: Skill for auto-formatting code to style standards
type: skill
language: python
---

# Style Formatter Skill

## Purpose
Auto-formats code files to ensure consistent style and conventions.

## Functions

### format_python(filepath, inplace=False)
Auto-format Python file using style guidelines.

**Parameters:**
- filepath (str): Path to Python file
- inplace (bool): Modify file directly (default False)

**Returns:**
- str: Formatted code (or file path if inplace=True)

**Formatting Applied:**
- Line wrapping (max 100 chars, 80 for code)
- Indentation (4 spaces)
- Spacing around operators
- Import organization (stdlib, third-party, local)
- Trailing whitespace removal
- Double blank lines between functions/classes

### format_html(filepath, inplace=False)
Auto-format HTML file.

**Parameters:**
- filepath (str): Path to HTML file
- inplace (bool): Modify file directly (default False)

**Returns:**
- str: Formatted code (or file path if inplace=True)

**Formatting Applied:**
- Indentation (2 spaces)
- Line breaks for readability
- Attribute formatting
- Tag closing
- Whitespace normalization

### format_css(css_content, inplace=False)
Auto-format CSS code.

**Parameters:**
- css_content (str): CSS code to format
- inplace (bool): Write back to file if string is path

**Returns:**
- str: Formatted CSS

**Formatting Applied:**
- Property indentation (2 spaces)
- Spacing around braces
- Selector formatting
- Color value normalization
- Property ordering (positioning, sizing, styling)

### format_json(filepath, inplace=False)
Format JSON for readability.

**Parameters:**
- filepath (str): Path to JSON file
- inplace (bool): Modify file directly (default False)

**Returns:**
- str: Formatted JSON

**Formatting Applied:**
- 2-space indentation
- Consistent property ordering
- Proper escaping

### add_docstrings(python_code)
Add missing docstrings to Python functions/classes.

**Parameters:**
- python_code (str): Python code

**Returns:**
- str: Code with docstrings added (template form)

**Format:**
```python
def function_name(param1, param2):
    """Brief description of what function does.
    
    Args:
        param1: Description
        param2: Description
    
    Returns:
        Description of return value
    """
```

### fix_naming_conventions(filepath, language)
Auto-fix common naming convention issues.

**Parameters:**
- filepath (str): File to fix
- language (str): 'python', 'html', 'css', or 'json'

**Returns:**
- str: Code with naming fixed

### apply_style_guide(filepath, standard='pep8')
Apply style guide to file.

**Parameters:**
- filepath (str): File to format
- standard (str): Style standard to apply

**Returns:**
- str: Formatted code

## Usage Example
```python
from style_formatter import format_python, format_html, format_json

py_code = format_python('scripts/fetch-arxiv.py', inplace=False)
html_code = format_html('arxiv-feed.html', inplace=False)
json_code = format_json('data/papers.json', inplace=False)
```

## Integration
Used by code-quality agent to auto-fix style issues before validation.
