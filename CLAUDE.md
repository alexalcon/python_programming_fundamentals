# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

A Python fundamentals learning repository that teaches Python concepts through algorithmic trading examples. All scripts are standalone and educational — they are not production trading code.

## Running scripts

All scripts run directly with Python. No build step, no virtual environment required beyond stdlib.

```bash
python <filename>.py
```

The one exception is the ch08 full trading system, which uses a local module import and must be run from inside its folder:

```bash
cd books_code/python_crash_course_book/ch08_functions/full_trading_system
python trading_functions_demo.py
```

## Repository structure

```
books_code/python_crash_course_book/   # Python Crash Course book exercises
    ch03_introducing_lists/            # List basics
    ch04_working_with_lists/           # Loops over lists
    ch08_functions/                    # Functions, *args/**kwargs, module imports
        full_trading_system/           # Multi-file demo combining ch08 concepts
        importing_functions/           # order_utils.py + trading_bot.py (module split)
    ch09_classes/                      # OOP: classes, inheritance, composition
        importing_classes/             # Class split across modules

structured_programming/               # Control flow exercises (numbered files)
    numerical_sequences/               # ns_01.py ... ns_04.py
    nested_control_flow_statements/    # mcfs_01.py ... mcfs_12.py
    2D_matrix_patterns/                # 2D_mp_01 ... 2D_mp_21 (matrix printing)
    iteration_statements/              # counter/sentinel-controlled loops

code_examples/                         # Standalone concept demos (fibonacci, exponential growth, etc.)
```

## Naming conventions

- `books_code` files: descriptive names tied to the book section (e.g. `trading_lists_demo.py`, `trading_strategy_inheritance.py`)
- `structured_programming` files: numbered sequence with short prefix (`ns_`, `mcfs_`, `2D_mp_`) plus a description; multiple approaches to the same problem use `_v1`, `_v2` suffixes
- Each `ch09_classes` file maps to a book subsection and its docstring header lists the covered topics

## Code style

Files follow a consistent structure:

- Module-level docstring with file name, author, description, and section list (ch09 style) or inline comments (structured_programming style)
- Phase comments for longer scripts: initialization phase → processing phase → main logic
- Print output uses thick/thin separator lines (`━━━` or `---`) to delimit sections
- Type hints used in ch09 classes files; absent in earlier chapters
- No external dependencies — stdlib only (`random` is the only import used so far)
