---
name: file-ops
description: Skill for file operations and I/O
type: skill
language: python
---

# File Operations Skill

## Purpose
Handles reading, writing, and managing project files safely and reliably.

## Functions

### read_json(filepath)
Read and parse JSON file.

**Parameters:**
- filepath (str): Path to JSON file

**Returns:**
- dict or list: Parsed JSON data

**Error Handling:**
- FileNotFoundError: Return empty dict
- JSONDecodeError: Log error, return empty dict

### write_json(filepath, data, pretty=True)
Write data to JSON file.

**Parameters:**
- filepath (str): Path to JSON file
- data (dict or list): Data to write
- pretty (bool): Format with indentation (default True)

**Returns:**
- bool: Success status

**Features:**
- Creates parent directories if needed
- Atomic write (write to temp, then move)
- Preserves backup of previous version

### read_file(filepath)
Read plain text file.

**Parameters:**
- filepath (str): Path to file

**Returns:**
- str: File contents

### write_file(filepath, content)
Write plain text file.

**Parameters:**
- filepath (str): Path to file
- content (str): Content to write

**Returns:**
- bool: Success status

### backup_file(filepath)
Create timestamped backup of file.

**Parameters:**
- filepath (str): File to backup

**Returns:**
- str: Path to backup file

**Format:**
- filename.backup.YYYY-MM-DD-HHmmss.ext

### ensure_directory(dirpath)
Create directory if it doesn't exist.

**Parameters:**
- dirpath (str): Directory path

**Returns:**
- bool: Success status

### list_files(dirpath, pattern=None)
List files in directory.

**Parameters:**
- dirpath (str): Directory to list
- pattern (str): Optional glob pattern

**Returns:**
- list: File paths

### file_exists(filepath)
Check if file exists.

**Parameters:**
- filepath (str): File path

**Returns:**
- bool: Exists status

## Usage Example
```python
from file_ops import read_json, write_json, backup_file

papers = read_json('data/papers.json')
backup_file('data/papers.json')
papers['last_updated'] = '2026-02-13T19:00:00Z'
write_json('data/papers.json', papers)
```

## Safety Features
- Backup before overwrite
- Atomic writes (temp + move)
- Safe path handling
- Permission checking
- Error recovery
