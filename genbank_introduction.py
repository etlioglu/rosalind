""" GenBank Introduction """

import sys
from typing import List

from Bio import Entrez

input_file: str = sys.argv[1]

with open(input_file, "r", encoding="utf-8") as file:
    lines: List[str] = file.readlines()

genus, date_from, date_to = lines


Entrez.email = "emre.etlioglu@gmail.com"

search_term: str = f'({genus}[Primary Organism]) AND ("{date_from}"[Publication Date] : "{date_to}"[Publication Date])'
handle = Entrez.esearch(db="nucleotide", term=search_term)

record: "Bio.Entrez.Parser.DictionaryElement" = Entrez.read(handle)

print(record["Count"])
