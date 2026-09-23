from pathlib import Path

ROOT = Path(__file__).parents[1]

EXPECTED_MODULES = [
    "01-python-basics",
    "02-control-flow",
    "03-data-structures",
    "04-functions",
    "05-oop",
    "06-exception-handling",
    "07-file-handling",
    "08-modules-packages",
    "09-regular-expressions",
    "10-iterators-generators",
    "11-decorators",
    "12-logging",
    "13-numpy",
    "14-pandas",
    "15-matplotlib",
    "16-seaborn",
    "17-plotly",
    "18-sql-pymysql",
    "19-eda",
    "20-pyspark",
]


def test_course_modules_exist():
    missing = [name for name in EXPECTED_MODULES if not (ROOT / name).is_dir()]
    assert not missing, f"Missing course modules: {missing}"


def test_core_course_files_exist():
    for path in ["README.md", "requirements.txt", "requirements-bigdata.txt", ".env.example"]:
        assert (ROOT / path).exists(), f"Missing required file: {path}"
