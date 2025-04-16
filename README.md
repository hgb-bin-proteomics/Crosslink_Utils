# Crosslink Utils

Helper scripts for crosslink analysis.

## Requirements

- Python 3.10+
- Packages as specified in [requirements.txt](https://github.com/hgb-bin-proteomics/Crosslink_Utils/blob/master/requirements.txt): `pip install -r requirements.txt`
- Or what is specified in the specific sub-directories!

## `find_shortest.py`

- Finds the shortest cross-linked residue pair per crosslink in a mulitmeric structure of proteins with equal sequences.
- A detailed description of the script parameters is given in the [script](https://github.com/hgb-bin-proteomics/Crosslink_Utils/blob/master/find_shortest.py).
- Example usage:
  ```
  python find_shortest.py data/pyXlinkViewer_export.py -c AB,CD -t 27.0
  ```
## MS Annika MS1 Error

An example implementation of calculating the MS1 Error for CSMs from [MS Annika](https://github.com/hgb-bin-proteomics/MSAnnika).

See notebook here: [ms1_error.ipynb](https://github.com/hgb-bin-proteomics/Crosslink_Utils/blob/master/01_MSAnnika_MS1_Error/ms1_error.ipynb)

## Proteome Discoverer Result File Reader

Automatically read in results from a
[Proteome Discoverer](https://www.thermofisher.com/at/en/home/industrial/mass-spectrometry/liquid-chromatography-mass-spectrometry-lc-ms/lc-ms-software/multi-omics-data-analysis/proteome-discoverer-software.html)
study and combine metrics
into a single table. In this example illustrated by reading numbers of peptide spectrum
matches, crosslink spectrum matches and crosslinks.

- Jupyter notebook: [see here](https://github.com/hgb-bin-proteomics/Crosslink_Utils/blob/master/02_pdResult_Reader/pdresult_reader.ipynb)
- Python script: [see here](https://github.com/hgb-bin-proteomics/Crosslink_Utils/blob/master/02_pdResult_Reader/pdresult_reader.py)

## Citing

If you are using scripts of this repository please cite [MS Annika](https://github.com/hgb-bin-proteomics/MSAnnika).

## License

- [MIT](https://github.com/hgb-bin-proteomics/Crosslink_Utils/blob/master/LICENSE)

## Contact

[micha.birklbauer@fh-hagenberg.at](mailto:micha.birklbauer@fh-hagenberg.at)
