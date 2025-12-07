import pathlib
import sys

import pytest

# Ensure project root is on the import path for direct execution
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from greet import greet, main


def test_greet_returns_message():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("")


def test_cli_outputs_greeting(capsys):
    main(["Ada"])
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Ada!"
