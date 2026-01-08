#!/usr/bin/env python3
#
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "pyteomics[XML]",
# ]
# ///

import argparse
from pyteomics import mgf

from typing import List
from typing import Dict

# mass_file = "data/masses.txt"
# mgf_file = "data/XLpeplib_Beveridge_QEx-HFX_DSS_R1.mgf"


def load_masses(mass_file: str) -> List[float]:
    with open(mass_file, "r", encoding="utf-8") as f:
        return [float(line.strip()) for line in f if line.strip()]


def count_masses(
    mgf_file: str, masses: List[float], tol: float = 0.02
) -> Dict[float, int]:
    counts = {m: 0 for m in masses}

    with mgf.read(mgf_file) as reader:
        for spectrum in reader:
            mz_values = spectrum["m/z array"]
            for query_mass in masses:
                if any(abs(query_mass - mz) < tol for mz in mz_values):
                    counts[query_mass] += 1
    return counts


def main(argv=None) -> Dict[float, int]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--spectra",
        dest="spectra",
        required=True,
        help="Mass spectra in .mgf format to search for the given masses.",
        type=str,
    )
    parser.add_argument(
        "-m",
        "--masses",
        dest="masses",
        required=True,
        help="Masses (or rather specific m/z values) to search the given mass spectra for.",
        type=str,
    )
    args = parser.parse_args(argv)
    masses = load_masses(args.masses)
    counts = count_masses(args.spectra, masses)

    print("Mass (m/z)   -> Count")
    print("---------------------")
    for m, c in counts.items():
        print(f"{m:<12} -> {c}")

    return counts


if __name__ == "__main__":
    m = main()
