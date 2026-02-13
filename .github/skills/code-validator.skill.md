---
name: code-validator
description: Skill for validating code syntax and style
type: skill
language: python
---

# Code Validator Skill

## Purpose
Validates syntax, style, and quality of generated code files.

## Functions

### validate_python(filepath)
Validate Python file syntax and style.

**Parameters:**
- filepath (str): Path to Python file

**Returns:**
- dict: Validation results

**Checks:**
- Syntax (compile to bytecode)
- PEP 8 style compliance via pylint
- Docstring presence for functions/classes
- Line length (max 100 chars, 80 for code)
- Import organization
- Naming conventions (snake_case)

**Output:**
```python
{
  "valid": bool,
  "errors": [...],      # Blocking issues
  "warnings": [...],    # Style issues
  "details": {...}      # Line numbers and messages
}
```

### validate_html(filepath)
Validate HTML file structure and accessibility.

**Parameters:**
- filepath (str): Path to HTML file

**Returns:**
- dict: Validation results

**Checks:**
- HTML5 validity (via html5lib)
- Semantic markup
- Accessibility (alt text, ARIA labels)
- Link validity (internal/external)
- Image references

### validate_json(filepath)
Validate JSON structure.

**Parameters:**
- filepath (str): Path to JSON file

**Returns:**
- dict: Validation results

**Checks:**
- Valid JSON syntax
- Required fields present
- Data type validation
- Proper escaping

### validate_css(css_content)
Validate CSS syntax and properties.

**Parameters:**
- css_content (str): CSS code to validate

**Returns:**
- dict: Validation results

**Checks:**
- CSS3 validity
- Color values
- Property names
- Selector syntax
- Animation properties

### check_naming_conventions(filepath)
Check naming conventions for file type.

**Parameters:**
- filepath (str): File to check

**Returns:**
- dict: Convention check results

**Rules:**
- Python: snake_case for variables/functions, PascalCase for classes
- HTML: kebab-case for IDs/classes
- CSS: kebab-case for selectors
- Constants: UPPER_SNAKE_CASE

### check_indentation(filepath)
Verify consistent indentation.

**Parameters:**
- filepath (str): File to check

**Returns:**
- dict: Indentation issues

**Standards:**
- Python: 4 spaces
- HTML/CSS: 2 spaces
- Tabs not allowed

## Usage Example
```python
from code_validator import validate_python, validate_html, validate_json

py_result = validate_python('scripts/fetch-arxiv.py')
html_result = validate_html('arxiv-feed.html')
json_result = validate_json('data/papers.json')

if not all([py_result['valid'], html_result['valid'], json_result['valid']]):
    print("Validation failed!")
```

## Integration
Used by code-quality agent to block commits if errors found.
