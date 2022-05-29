import pytest
from app.util import clean_dna, valid_dna


def test_clean_dna():
    dna = " AcT "
    assert clean_dna(dna) == "ACT"


def test_valid_dna():
    dna = "ACT"
    assert valid_dna(dna) == True


def test_invalid_dna():
    dna = "EACT"
    assert valid_dna(dna) == False
