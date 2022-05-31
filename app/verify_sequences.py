from constants import VALID_NUCLEOTIDE_SEQ, VALID_PROTEIN_SEQ

def clean_sequence(seq: str) -> str:
    return seq.upper().strip()


def valid_dna(dna: str) -> bool:
    full_dna_seq = set(VALID_NUCLEOTIDE_SEQ)
    if set(dna).union(full_dna_seq) != full_dna_seq:
        return False
    return True


def valid_protein(protein: str) -> bool:
    full_protein_seq = set(VALID_PROTEIN_SEQ)
    if set(protein).union(full_protein_seq) != full_protein_seq:
        return False
    return True