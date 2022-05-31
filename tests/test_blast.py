import os
import sys
import pytest
sys.path.append(os.path.abspath('app'))
from blast import blast

@pytest.mark.asyncio
async def test_blast_ginkgo_example():
    blast_result = await blast('CCTTTTCTCTCGAGCGGAGGGAAAACGGAA')
    assert blast_result.dna == 'CCTTTTCTCTCGAGCGGAGGGAAAACGGAA'
    assert blast_result.genome == 'NC_000852'
    assert blast_result.protein == 'NP_048806.1'
    assert blast_result.match == 'FSLERRENG'


@pytest.mark.asyncio
async def test_blast_custom_example():
    blast_result = await blast('ACCGATGAAGCGAGGACCGGCCGACACCTTCTTCCCCACGATAGA')
    assert blast_result.dna == 'ACCGATGAAGCGAGGACCGGCCGACACCTTCTTCCCCACGATAGA'
    assert blast_result.genome == 'NC_027867'
    assert blast_result.protein == 'YP_009165003.1'
    assert blast_result.match == 'PMKRGPADTFFPTI'


@pytest.mark.asyncio
async def test_blast_empty():
    blast_result = await blast('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    assert blast_result == None