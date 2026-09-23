# Migration & Curation Map

The new course is a curated migration from B07_Python. The legacy repository remains unchanged.

## Migrated lessons

| New module | Curated source material |
|---|---|
| 01 Python Basics | Day3, Day4 |
| 02 Control Flow | Day5, Day6_A |
| 03 Data Structures | Day7, Day8, Day9, Day11-set, Day12 Dict |
| 04 Functions | Day10, Day13- Function, Day14 -lambda |
| 05 OOP | Day16-oop1 |
| 06 Exceptions | Day20-Exception |
| 07 File Handling | FileHandling |
| 12 Logging | python_logging_complete_tutorial, logging_quick_reference, logging_comparison_guide |
| 13 NumPy | NumpyComprehensive, NumpyWorkbook |
| 14 Pandas | PandasUltimate, PandasHandBook, Merge_Concat |
| 15 Matplotlib | Matplotlib |
| 16 Seaborn | Seaborn |
| 17 Plotly | Plotly |
| 18 SQL / PyMySQL | Eda and pymysql |
| 19 EDA | EDA |
| 20 PySpark | pyspark |

## Curation rules applied

- Notebook execution outputs removed.
- Execution counters reset.
- Lessons renamed to descriptive names instead of Day-number filenames.
- Database credential-like values replaced with environment-variable placeholders.
- Large duplicate notebooks were not copied blindly.
- The old virtual environment was not migrated.
- Generated log files were not migrated.
- Temporary and empty scratch files were not migrated.
- Binary Excel/PDF artifacts are not copied automatically; reusable teaching data is migrated selectively.

## Next curation pass

1. Split oversized notebooks into focused lessons.
2. Add explanations before major code blocks.
3. Add practice tasks after each concept.
4. Add expected outcomes and interview questions.
5. Add 100+ structured labs.
6. Add project-specific datasets only where licensing permits.