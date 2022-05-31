from pydantic import BaseModel

class BlastResult(BaseModel):
    dna: str
    genome: str
    protein: str
    match: str