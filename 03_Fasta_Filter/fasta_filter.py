#!/usr/bin/env python3
#
# /// script
# requires-python = ">=3.7"
# dependencies = [
#   "biopython",
# ]
# ///

# FASTA FILTER
# 2025 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

from Bio import SeqIO


def fasta_filter(fasta_file: str) -> str:
    records = list()
    for record in SeqIO.parse(fasta_file, "fasta"):
        records.append(record)
    print(f"Read {len(records)} sequences from fasta file {fasta_file}!")
    unique_records = dict()
    for record in records:
        seq = str(record.seq)
        if "X" not in seq.upper():
            if seq not in unique_records:
                unique_records[seq] = record
            else:
                # pass because duplicate sequence
                pass
        else:
            # pass because ambiguous
            pass
    records_to_write = list(unique_records.values())
    SeqIO.write(records_to_write, f"{fasta_file}_unique_seq_no_X.fasta", "fasta")
    diff = len(records) - len(records_to_write)
    print(f"Filtered out {diff} sequences because of duplicate or ambiguous sequences!")
    print(f"Filtered fasta file contains {len(records_to_write)} sequences!")
    print(f"Wrote fasta file with name {fasta_file}_unique_seq_no_X.fasta!")
    print("Finished successfully!")
    return f"{fasta_file}_unique_seq_no_X.fasta"


if __name__ == "__main__":
    import sys

    _ = fasta_filter(sys.argv[1])
