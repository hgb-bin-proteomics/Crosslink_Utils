# Crosslink Utils

Helper scripts for crosslink analysis.

## Requirements

- Python 3.10+
- Packages as specified in [requirements.txt](https://github.com/hgb-bin-proteomics/Crosslink_Utils/blob/master/requirements.txt): `pip install -r requirements.txt`

## `find_shortest.py`

- Finds the shortest cross-linked residue pair per crosslink in a mulitmeric structure of proteins with equal sequences.
- A detailed description of the script parameters is given in the [script](https://github.com/hgb-bin-proteomics/Crosslink_Utils/blob/master/find_shortest.py).
- Example usage:
  ```
  python find_shortest.py data/pyXlinkViewer_export.py -c AB,CD -t 27.0
  ```

## License

- [MIT](https://github.com/hgb-bin-proteomics/Crosslink_Utils/blob/master/LICENSE)

## Contact

[micha.birklbauer@fh-hagenberg.at](mailto:micha.birklbauer@fh-hagenberg.at)
