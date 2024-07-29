import pytest
from katas.kyu8.abbreviated_name import abbrev_name

def test_abbrev_name():
        assert abbrev_name("hersey nageye") == "H.N"
        assert abbrev_name("patrick freeman") == "P.F"
        assert abbrev_name("Evan C") == "E.C"
        assert abbrev_name("d Trump") == "D.T"