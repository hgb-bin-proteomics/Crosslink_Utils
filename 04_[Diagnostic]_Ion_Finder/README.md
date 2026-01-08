# \[Diagnostic\] Ion Finder

Counts in how many mass spectra the specified m/z values appear (e.g. to find diagnostic ions). Mass spectra should be given
in `.mgf` format. Masses should be given in a single `.txt` file with one mass per line. The script simply matches the masses
to the m/z array of every mass spectrum. No deisotoping or deconvolution is performed.

## Usage

Requires [python](https://www.python.org/downloads/) or **recommended** [uv](https://docs.astral.sh/uv/)!

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
- Run the script with:
  ```bash
  uv run count_matched_spectra.py -s spectra.mgf -m masses.txt
  ```
- For example:
  ```bash
  uv run count_matched_spectra.py -s data/XLpeplib_Beveridge_QEx-HFX_DSS_R1.mgf -m data/masses.txt
  ```
- The script will display for each mass in how many mass spectra it was detected.

## Contact

- [micha.birklbauer@fh-hagenberg.at](mailto:micha.birklbauer@fh-hagenberg.at)
