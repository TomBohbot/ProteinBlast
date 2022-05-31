from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def dna_seq_to_fasta() -> None:
    records = []
    for genome in ['NC_000852', 'NC_007346', 'NC_008724', 'NC_009899', 'NC_014637', 'NC_020104', 'NC_023423', 'NC_016072', 'NC_023719', 'NC_027867']:
        with open(f'app/data/raw_data/{genome}.txt','r') as file:
            protein_id = None
            translation = None
            translation_in_prog = False
            for line in file:
                if protein_id and translation and translation_in_prog == False:
                    records.append(SeqRecord(
                        Seq(translation.replace('"', '').replace('\n', '')),
                        id=protein_id.replace('"', ''),
                        name=protein_id,
                        description=genome
                    ))
                    protein_id = None
                    translation = None
                if 'protein_id' in line:
                    protein_id = line.split('=')[1]
                if 'gene' in line:
                    translation_in_prog = False                
                if translation_in_prog == True:
                    translation = "".join([translation,line])
                if '/translation' in line:
                    translation = line.split('=')[1].replace('"', '').strip()
                    translation_in_prog = True
            if protein_id and translation and translation_in_prog == False:
                records.append(SeqRecord(
                    Seq(translation.replace('"', '').replace('\n', '')),
                    id=protein_id.replace('"', ''),
                    name=protein_id,
                    description=genome
                ))
    with open('app/data/database/database.fasta', "w") as output_handle:
        SeqIO.write(records, output_handle, "fasta")


# dna_seq_to_fasta()