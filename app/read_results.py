from models import BlastResult
from bs4 import BeautifulSoup
from constants import BLAST_HITS, BLAST_HIT_TYPES,    \
    BLAST_HIT_SEQ, OUTPUT_FILE_PATH, BLAST_ERROR_KEY

def no_results(xml: BeautifulSoup) -> bool:
    hit = xml.find(BLAST_HITS)
    error_message = xml.find(BLAST_ERROR_KEY)
    if len(hit.get_text()) == 1 and error_message.get_text() != None:
        return True
    return False


def read_blast_results(dna: str, file_path: str = OUTPUT_FILE_PATH) -> BlastResult:
    soup = BeautifulSoup(open(file_path,'r'), 'xml')
    if no_results(soup):
        return None  
    hit = soup.find(BLAST_HITS)     
    return BlastResult(
        dna=dna,
        genome=hit.find(BLAST_HIT_TYPES).get_text().split()[1], 
        protein=hit.find(BLAST_HIT_TYPES).get_text().split()[0],
        match=hit.find(BLAST_HIT_SEQ).get_text() 
    )