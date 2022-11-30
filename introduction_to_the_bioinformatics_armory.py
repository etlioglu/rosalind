# Introduction to the Bioinformatics Armory
# https://rosalind.info/problems/ini/

from Bio.Seq import Seq

dna_string: str = input("Enter DNA sequence:")

dna_seq: Seq = Seq(dna_string.upper())

print(
    dna_seq.count("A"),
    dna_seq.count("C"),
    dna_seq.count("G"),
    dna_seq.count("T"),
)
