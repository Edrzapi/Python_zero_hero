# Python Zero to Hero

A structured teaching repository covering Python from first principles through to object-oriented programming, data handling, and testing. Each topic is a self-contained module with runnable examples and in-code commentary.

---

## Who Is This For?

- Beginners learning Python for the first time
- Delegates on instructor-led Python fundamentals courses
- Self-learners who want a clear, progressive syllabus to follow

No prior Python experience is assumed. Basic comfort with a command line is helpful.

---

## Prerequisites

| Tool   | Minimum Version |
|--------|----------------|
| Python | 3.10+          |

```bash
python --version
```

---

## Getting Started

### Option 1: Virtual Environment (Recommended)

```bash
# Clone the repository
git clone git@github.com:Edrzapi/Python_zero_hero.git
cd Python_zero_hero

# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Install Directly

If you prefer not to use a virtual environment:

```bash
git clone git@github.com:Edrzapi/Python_zero_hero.git
cd Python_zero_hero
pip install -r requirements.txt
```

> **Note:** Most modules use only the standard library. The `requirements.txt` covers the data I/O and API modules that need `requests`, `SQLAlchemy`, `pandas`, and `mysql-connector-python`.

---

## Repository Structure

```
├── basics/                 # Primitives, strings, type conversion
├── collections/            # Lists, tuples, sets, dicts, comprehensions
├── control_flow/           # Conditionals, comprehensions
├── iteration/              # for, while, foreach, itertools
├── functions/              # Parameters, scope, lambdas, decorators
├── oop/                    # Classes, inheritance, MRO, abstraction
├── exceptions/             # Try/except, custom exceptions
├── io/                     # File I/O, JSON, CSV
├── databases/              # SQLite, SQLAlchemy
├── apis/                   # HTTP requests with the requests library
├── testing/                # Doctests, unittest, test suites
├── module_packages/        # Package structure and imports
├── tasks/                  # Hands-on exercises
│   ├── calculator/         # OOP calculator with unit tests
│   ├── garage/             # Inheritance project with test suite
│   ├── comprehension_task/ # Comprehension practice
│   └── palindrome/         # String manipulation exercise
└── main.py                 # Entry point
```

---

## Topics Covered

### Core Language

- **Data Types** — Integers, floats, strings, booleans. Lists, tuples, sets, dictionaries. Mutability, iteration, common operations.
- **Control Flow** — `if`/`elif`/`else`, `for` and `while` loops, `break`/`continue`, list/set/dict comprehensions.
- **Functions** — Defining functions, positional and keyword arguments, `*args`/`**kwargs`, scope, lambda functions, decorators.

### Object-Oriented Programming

- **Classes and Objects** — `__init__`, attributes, methods, encapsulation.
- **Inheritance** — Single and multiple inheritance, method resolution order (MRO).
- **Abstraction** — Abstract base classes, interface patterns.

### Error Handling

- **Exception Handling** — `try`/`except`/`finally`, raising exceptions, custom exception classes.

### Data and I/O

- **File Handling** — Reading and writing text files, context managers (`with` statement).
- **Structured Data** — JSON and CSV processing.
- **Databases** — SQLite with raw SQL, introduction to SQLAlchemy.
- **APIs** — HTTP GET requests using the `requests` library.

### Testing

- **Doctests** — Inline test examples in docstrings.
- **unittest** — Test classes, assertions, setup/teardown.
- **Test Suites** — Grouping and running multiple test modules.

### Practical Tasks

Each task applies multiple concepts together:

| Task | Concepts Practiced |
|------|--------------------|
| Calculator | OOP, user input, unit testing |
| Garage | Inheritance, polymorphism, test suites |
| Comprehensions | List/set/dict comprehension patterns |
| Palindrome | String manipulation, logic |

---

## How to Run

Each module can be run directly:

```bash
python basics/basic_datatypes.py
python functions/intro_func.py
python oop/Inheritance.py
```

Run the calculator task:
```bash
python tasks/calculator/Menu.py
```

Run the garage test suite:
```bash
python tasks/garage/testing/GarageTestSuite.py
```

Run unit tests:
```bash
python -m unittest testing/intro_to_unittest.py
```

---

## Teaching Approach

- Each file is a standalone, runnable example
- Concepts are explained in comments alongside working code
- Topics progress from simple to complex within each module
- Tasks give delegates a chance to apply what they've learned
- Third-party libraries are introduced only where they serve a teaching purpose (requests, SQLAlchemy, pandas)

---

## Tech Stack

| Technology             | Purpose                                  |
|------------------------|------------------------------------------|
| Python 3.10+           | Language                                 |
| unittest               | Testing framework (stdlib)               |
| SQLite                 | Embedded database (stdlib)               |
| SQLAlchemy 2.0+        | ORM introduction                         |
| requests               | HTTP client library                      |
| pandas                 | CSV chunked processing                   |
| mysql-connector-python | MySQL driver (used with SQLAlchemy)      |

No Django. No Flask. No Jupyter. No notebooks.

---

## What's Next?

This course covers Python fundamentals and OOP. For applied Python topics — web development, data engineering, automation — see the applied course repositories in this family.

For the same structured approach in other languages, see the companion repositories:

- [Java Zero to Hero](https://github.com/Edrzapi/Java_zero_hero)
- [C# Zero to Hero](https://github.com/Edrzapi/CS_zero_hero)
