# Lesson 5: SQLAlchemy ORM - Student Assignments

## Setup Instructions

### 1. Environment Setup
```bash
# Create a virtual environment
python -m venv venv

# Activate the environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install SQLAlchemy
pip install sqlalchemy
```

### 2. Basic Setup Code
```python
from sqlalchemy import create_engine, String, DateTime, Text, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Mapped, mapped_column
from datetime import datetime, timedelta

# Create engine and base
engine = create_engine('sqlite:///assignments.db', echo=True)
Base = declarative_base()

# Create all tables
Base.metadata.create_all(engine)
```

---
## Assignment 1: Basic Setup and Single Model (20 minutes)

**Goal**: Get familiar with SQLAlchemy setup and create your first model.

### Setup Instructions
1. Create a new Python file called `assignment1.py`
2. Install SQLAlchemy: `pip install sqlalchemy`
3. Set up the basic imports and database connection

### Required Tasks
```python
# TODO: Complete this setup code
from sqlalchemy import create_engine, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column
from datetime import datetime

# TODO: Create engine and base

# TODO: Create a simple Student model with these fields:
# - id (primary key)
# - first_name (string, required)
# - last_name (string, required)
# - student_id (string, unique, required)
# - enrollment_date (datetime, default to current time)
# - is_active (boolean, default to True)

# Add the table to the db

```

### Success Criteria
- [ ] SQLAlchemy is installed and imported correctly
- [ ] Database connection is established
- [ ] Student model is created with modern declarative mapping
- [ ] Table is created in the database


---

## Assignment 2: Multiple Models and Relationships (20 minutes)

**Goal**: Create multiple models and establish relationships between them.

### Setup Instructions
1. Create a new Python file called `assignment2.py`
2. Use the same setup as Assignment 1

### Required Tasks
```python
# TODO: Create these models with relationships

# 1. Department model:
# - id (primary key)
# - name (string, required)
# - location (string, optional)

# 2. Course model:
# - id (primary key)
# - code (string, required, unique)
# - title (string, required)
# - credits (integer, required)
# - department_id (foreign key to Department)
# - relationship to Department

# 3. Add relationship in Department:
# - courses (one-to-many relationship to Course)

# TODO: Create tables

```

### Success Criteria
- [ ] Department and Course models are created
- [ ] Foreign key relationship is established
- [ ] Bidirectional relationship is set up
- [ ] Sample data is added successfully
- [ ] Query shows courses with their department information
- [ ] No errors when running the script

---