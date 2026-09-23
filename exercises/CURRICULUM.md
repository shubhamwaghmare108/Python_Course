# Lab Curriculum Guide

## Learning progression

| Stage | Labs | Focus | Expected outcome |
|---|---:|---|---|
| Beginner | 1–35 | Python syntax, types, collections, control flow | Write small correct programs independently |
| Intermediate | 36–65 | Functions, OOP, files, errors | Build reusable and defensive Python programs |
| Advanced | 66–100 | NumPy, Pandas, visualization, SQL, PySpark, EDA | Complete data-analysis workflows |

## Standard lab workflow

For every lab, students should submit:
1. Solution — `.py` file or notebook.
2. Test cases — at least 3 normal cases and 2 edge cases where applicable.
3. Explanation — 3–5 sentences describing the approach.
4. Evidence — expected output, table, chart, or query result.
5. Extension — one improvement beyond the minimum requirement.

## Acceptance criteria

- Required behavior works.
- Relevant inputs are validated.
- Edge cases are handled explicitly.
- Names and structure are readable.
- No machine-specific paths are required.
- Data-analysis labs document assumptions.
- SQL labs use parameterized queries for user-provided values.
- Database credentials come from environment variables.
- Charts have titles, axis labels, and appropriate chart types.

## Recommended assessment rubric

| Criterion | Points |
|---|---:|
| Correctness | 40 |
| Edge cases / validation | 15 |
| Code quality | 15 |
| Explanation | 10 |
| Testing / evidence | 10 |
| Extension | 10 |
| **Total** | **100** |

## Dataset progression

- Python basics: generated values and user input.
- Collections/control flow: generated lists, dictionaries, and records.
- NumPy: generated arrays and numerical simulations.
- Pandas: `datasets/titanic_demo.csv`.
- Visualization/EDA: Titanic or another small CSV supplied by the instructor.
- SQL/PyMySQL: instructor-provided local database schema; credentials must come from `.env`.
- PySpark: generated DataFrames or small local CSV/Parquet files.

## Instructor workflow

**Teach → Demonstrate → Guided lab → Independent lab → Extension → Review**

Keep instructor solutions separate from the student-facing repository.

## Definition of done

A lab should require at least one decision: choose a data structure, validate an input, select a transformation, choose a chart, construct a query, interpret an output, or explain a trade-off.