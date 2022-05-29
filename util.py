def clean_dna(dna: str) -> str:
    return dna.upper().strip()

def valid_dna(dna: str) -> bool:
    if set(dna).union(set("ACTG") ) != set("ACTG"):
        return False
    return True