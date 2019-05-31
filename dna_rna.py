#!/usr/bin/python3

dna_charset = "ATGC"
rna_charset = "UACG"

dna_sequence = "AATTCCCCG"

translator = str.maketrans(dna_charset, rna_charset)

print (dna_sequence.translate(translator))