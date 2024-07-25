import pytest
from katas.kyu8.make_uppercase import make_upper_case

def test_make_upper_case():
    assert make_upper_case("hello") == "HELLO"
    assert make_upper_case("world") == "WORLD"
    assert make_upper_case("Python") == "PYTHON"
    assert make_upper_case("") == ""
    assert make_upper_case("123") == "123"
    assert make_upper_case("hello world") == "HELLO WORLD"
