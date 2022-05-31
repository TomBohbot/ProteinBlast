import os
import sys
sys.path.append(os.path.abspath('app'))
from verify_sequences import clean_sequence, valid_dna, valid_protein

def test_clean_seq():
    assert clean_sequence(" AcT ") == "ACT"


def test_valid_dna():
    assert valid_dna("ACT") == True


def test_invalid_dna():
    assert valid_dna("EACT") == False


def test_valid_protein():
    assert valid_protein("ASDFGHKL") == True


def test_invalid_protein():
    assert valid_protein("ASDFGHJKLQWERTYUIOPZXCVBNM") == False