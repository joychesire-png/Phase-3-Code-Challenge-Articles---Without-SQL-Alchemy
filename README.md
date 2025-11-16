# Phase-3-Code-Challenge-Articles---Without-SQL-Alchemy

# Magazine Domain Project (Python OOP)

This is a small Python project that models a simple magazine publishing system.  
The goal was to practice Object-Oriented Programming (OOP), work with classes,  
and understand relationships between objects.

The project contains three main classes:

- **Author** – a writer who creates articles
- **Magazine** – a publication that contains articles
- **Article** – connects an Author and a Magazine, and has a title

An Author can have many Articles, a Magazine can have many Articles,  
and an Article belongs to both an Author and a Magazine.

---

## Project Structure

project-root/
├── lib/
│ ├── article.py
│ ├── author.py
│ ├── debug.py
│ └── magazine.py
├── tests/
│ ├── **init**.py
│ ├── article_test.py
│ ├── author_test.py
│ └── magazine_test.py
├── LICENSE
├── Pipfile
├── pipfile.lock
├── pytest.ini
└── README.md

## How to Run

### 1. Install dependencies

pipenv install

### 2. Enter the virtual environment

pipenv shell

### 3. Run tests

pytest

### 4. Test your code manually

python lib/debug.py

You can create objects in `debug.py` and try your methods to see how they work.

---

## Description of Classes

### **Author**

- Has a name (cannot be changed after creation)
- Can list all articles they wrote
- Can list all magazines they’ve contributed to
- Can create a new Article

### **Magazine**

- Has a name (2–16 characters) and a category
- Can list all articles published
- Can list all authors who contributed
- Can show all article titles

### **Article**

- Has a title (5–50 characters, cannot be changed)
- Belongs to one Author and one Magazine

---

## What You Will Learn

- Creating and using Python classes
- Validating input using properties
- Connecting objects with relationships
- Storing and searching for related objects
- Using pytest to test your work
- Experimenting in a manual debug file

---

## Purpose of the Project

This project helps you practice:

- Python classes and instances
- Object relationships
- Aggregate and association methods
- Running and passing automated tests
- Writing clean and working code

---

## Status

All core methods are implemented and tested.  
You can experiment in `lib/debug.py` to try out the classes and methods.
