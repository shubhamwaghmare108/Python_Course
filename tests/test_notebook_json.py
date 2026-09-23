import ast
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]


def notebook_paths():
    return sorted(ROOT.rglob("*.ipynb"))


@pytest.mark.parametrize("path", notebook_paths())
def test_notebook_is_valid_json(path):
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    assert data.get("nbformat") in (4, 5)
    assert isinstance(data.get("cells"), list)
    for index, cell in enumerate(data["cells"]):
        assert cell.get("cell_type") in {"code", "markdown", "raw"}
        assert isinstance(cell.get("source"), list)

        if cell.get("cell_type") == "code":
            source = "".join(cell["source"])
            if source.strip():
                ast.parse(source, filename=f"{path}:cell-{index}")
