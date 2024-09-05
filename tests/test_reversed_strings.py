import pytest
from katas.kyu8.reversed_strings import solution

def test_reversed_string():
    assert solution("hersey") == "yesreh"
    assert solution("oli") == "ilo"
    assert solution("andrew") == "werdna"
    assert solution("lukasz") == "zsakul"