from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from read_results import read_blast_results
from Bio.Blast.Applications import NcbiblastxCommandline
from constants import INPUT_FILE_PATH, DB_PATH, E_VALUE, OUTFMT, OUTPUT_FILE_PATH, \
    INPUT_ID, INPUT_NAME, INPUT_DESC

def dna_seq_to_fasta(dna: str) -> str:
    record = SeqRecord(
        Seq(dna),
        id=INPUT_ID,
        name=INPUT_NAME,
        description=INPUT_DESC,
    )    
    with open(INPUT_FILE_PATH, "w") as output_handle:
        SeqIO.write(record, output_handle, "fasta")

async def blast(dna: str) -> dict:
    # Create fasta file to compare input to database:
    dna_seq_to_fasta(dna)
    # Run blastx command as it sequences nucleotide to protein.
    NcbiblastxCommandline (
        query=INPUT_FILE_PATH,
        db=DB_PATH,
        evalue=E_VALUE,
        outfmt=OUTFMT,
        out=OUTPUT_FILE_PATH
    )()
    return read_blast_results(dna)