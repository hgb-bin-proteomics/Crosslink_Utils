# Fasta Filter

Filters out duplicate proteins and proteins with ambiguous sequences (e.g. containing amino acid letter code `"X"`) from a FASTA file
and writes a new FASTA file with suffix `"_unique_seq_no_X.fasta"`.

## Usage

Requires [python](https://www.python.org/downloads/) or **recommended** [uv](https://docs.astral.sh/uv/)!

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
- Run the script with:
  ```bash
  uv run fasta_filter.py your_fasta_file.fasta
  ```
- For example:
  ```bash
  uv run fasta_filter.py ecoli_human.fasta
  ```
- The script will display how many sequences are filtered out and write a new FASTA file with name `{your_fasta_file.fasta}_unique_seq_no_X.fasta` that without the filtered out proteins.
- From the above example you would get a new file named: `ecoli_human.fasta_unique_seq_no_X.fasta`

## Contact

- [micha.birklbauer@fh-hagenberg.at](mailto:micha.birklbauer@fh-hagenberg.at)
