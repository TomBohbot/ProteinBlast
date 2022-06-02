Potein Blast
====

Protein Blast is a web application that can determine whether a particular DNA strand
matches any part of the DNA sequences that could encode a protein in a well-known set.

The web app returns the matching genome, protein, and start and end position of where
the subsequence was found in the protein’s sequence, and displays previous queries in 
the home page.

To be able to find if a DNA strand matches we use blastx which is a commandline in
biopython.

Protein Blast uses 10 genomes as its database which are (NC_016072 replaced NC_023640 in NCBI):
NC_000852, NC_007346, NC_008724, NC_009899, NC_014637, NC_020104, NC_023423, NC_016072, NC_023719, NC_02786

Try it using Docker
-------------------

To start the Protein Blast server:

    docker build -t protein-blast . && docker run -p 5000:5000 protein-blast

Then check it out in your browser: http://127.0.0.1:5000/ .

Once you are in the website you can input any DNA sequence and see the protein
match if it exists.
