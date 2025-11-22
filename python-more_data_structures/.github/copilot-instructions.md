# Copilot Instructions for AI Coding Agents

## Project Overview
This repository contains Python scripts focused on data structures, specifically sets and dictionaries. Each file implements a distinct function or algorithm, with corresponding `*-main.py` files serving as entry points or test drivers.

## File Structure & Patterns
- **No Classes**: All logic is implemented as standalone functions, not classes.

- **Testing**: Run any `*-main.py` file directly to test the corresponding function. Example:
  ```bash
  python3 0-main.py
- **Adding Functions**: To add a new function, create both a `N-function_name.py` and a `N-main.py` file, following the existing naming pattern.

- **No External Dependencies**: Do not add third-party packages.
- **Simple Data Structures**: Favor built-in Python types (list, set, dict).

## Key Files
- `README.md`: Brief project description.
- `*-main.py`: Test/entry points for each function.
- `*-function.py`: Implementation of each exercise/function.
```python
# 0-square_matrix_simple.py
# 0-main.py
from 0-square_matrix_simple import square_matrix_simple
- Always follow the file naming and function structure conventions.
- Avoid introducing classes, frameworks, or external dependencies.
- Keep code readable and idiomatic to Python.
