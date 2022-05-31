import os
import sys
from bs4 import BeautifulSoup
sys.path.append(os.path.abspath('app'))
from read_results import no_results, read_blast_results

def test_no_results_true():
    xml = BeautifulSoup(open('tests/fixtures/blast_results/zero_blast_results.xml','r'), 'xml')
    assert no_results(xml) == True


def test_no_results_False():
    xml = BeautifulSoup(open('tests/fixtures/blast_results/one_blast_result.xml','r'), 'xml')
    assert no_results(xml) == False


def test_read_empty_blast_result():
    assert read_blast_results("ACTG", 'tests/fixtures/blast_results/zero_blast_results.xml') == None


def test_read_filled_blast_result():
    blast_result = read_blast_results("ACTG", 'tests/fixtures/blast_results/one_blast_result.xml')
    assert blast_result.dna == "ACTG"
    assert blast_result.genome == "NC_027867"
    assert blast_result.protein == "YP_009165003.1"
    assert blast_result.match == "PMKRGPADTFFPTI"