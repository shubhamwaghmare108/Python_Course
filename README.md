# Python Course

A structured, classroom-ready Python curriculum curated from the teaching material in B07_Python.

## Learning path

01 Python Basics → 02 Control Flow → 03 Data Structures → 04 Functions → 05 OOP → 06 Exceptions → 07 File Handling → 08 Modules → 09 Regular Expressions → 10 Iterators/Generators → 11 Decorators → 12 Logging → 13 NumPy → 14 Pandas → 15 Matplotlib → 16 Seaborn → 17 Plotly → 18 SQL/PyMySQL → 19 EDA → 20 PySpark.

## Curation philosophy

The source material is curated rather than copied wholesale. Large notebooks are split into focused lessons, execution output is removed, machine-specific paths are excluded, and database examples use environment variables.

## Practice

The repository now contains **100 structured labs** across beginner, intermediate, and advanced levels. Each lab includes an implementation task, edge case, extension challenge, and interview question.

## Setup

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For PySpark: `pip install -r requirements-bigdata.txt`.

Copy `.env.example` to `.env` for local configuration. Never commit `.env`.

## Repository map

- `01-* ... 20-*`: curriculum
- `exercises/`: 100 labs
- `datasets/`: teaching datasets
- `projects/`: capstones
- `MIGRATION.md`: migration decisions
- `ROADMAP.md`: course evolution

The legacy B07_Python repository remains the source archive; this repository is the curated student-facing course.
