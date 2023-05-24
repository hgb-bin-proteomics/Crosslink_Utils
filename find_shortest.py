#!/usr/bin/env python3

# FIND SHORTEST RESIDUE PAIR/CROSSLINK
# 2023 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

# version tracking
__version = "1.0.0"
__date = "2023-05-24"

# requirements
# pip install pandas

# import packages
import argparse
import pandas as pd

from typing import List

def find_shortest(input: str, equal_chains: List[List[str]] | None = None, ignore_zero_links: bool = True) -> pd.DataFrame:

    df = pd.read_csv(input)
    equal_chains_mapping = dict()
    crosslinks = dict()

    if equal_chains is not None:
        for chains in equal_chains:
            for chain in chains:
                if chain not in equal_chains_mapping:
                    equal_chains_mapping[chain] = chains[0]

    chains_in_df = set(df["Chain 1"].tolist() + df["Chain 2"].tolist())
    for chain in chains_in_df:
        if str(chain) not in equal_chains_mapping:
            equal_chains_mapping[str(chain)] = str(chain)

    for i, row in df.iterrows():
        key = equal_chains_mapping[str(row["Chain 1"])] + str(row["Residue 1"]) + equal_chains_mapping[str(row["Chain 2"])] + str(row["Residue 2"])
        if ignore_zero_links and float(row["CA distance"]) == 0.0:
            continue
        if key not in crosslinks:
            crosslinks[key] = {float(row["CA distance"]): i}
        else:
            crosslinks[key][float(row["CA distance"])] = i

    index_to_keep = []
    for xl in crosslinks:
        shortest = min(crosslinks[xl].keys())
        index_to_keep.append(crosslinks[xl][shortest])

    return df.iloc[index_to_keep]

def export_to_pyXlinkViewer(shortest: pd.DataFrame, output_file: str) -> str:

    file_content = ""

    for i, row in shortest.iterrows():
        file_content += str(row["Chain 1"]) + "|" + str(row["Residue 1"]) + "|" + str(row["Chain 2"]) + "|" + str(row["Residue 2"]) + "\n"

    with open(output_file, "w", encoding = "utf-8") as f:
        f.write(file_content)
        f.close()

    return file_content

def export_to_PAEViewer(shortest: str, output_file: str, threshold: float | None = None) -> pd.DataFrame:

    import urllib.request as ur

    ur.urlretrieve("https://raw.githubusercontent.com/hgb-bin-proteomics/MSAnnika_exporters/master/PAEViewerExporter_msannika.py", "PAEViewerExporter_msannika.py")

    from PAEViewerExporter_msannika import MSAnnika_Exporter as Exporter

    exporter = Exporter(shortest, threshold)

    return exporter.export(output_file)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(metavar = "f",
                        dest = "file",
                        help = "Name/Path of the pyXlinkViewer result file to process.",
                        type = str,
                        nargs = 1)
    parser.add_argument("-c", "--equal-chains",
                        dest = "chains",
                        default = None,
                        help = "Chains that should be considered equal because they have the same sequence. E.g. AB, CD if A and B are the same protein and C and D are the same protein.",
                        type = str)
    parser.add_argument("-z", "--allow-zeros",
                        dest = "allow_zeros",
                        action = "store_false",
                        help = "Allow zero length crosslinks.")
    parser.add_argument("-t", "--threshold",
                        dest = "threshold",
                        default = None,
                        help = "Threshold that specifies if a crosslink satisfies the crosslinker-specific distance constraint.",
                        type = float)
    parser.add_argument("-o", "--output",
                        dest = "output",
                        default = None,
                        help = "Name of the output file.",
                        type = str)
    parser.add_argument("--version",
                        action = "version",
                        version = __version)
    args = parser.parse_args()

    chains_param = [[chain for chain in chains.strip()] for chains in args.chains.split(",")] if args.chains is not None else None

    shortest = find_shortest(args.file[0], chains_param, args.allow_zeros)

    output = args.file[0].split(".csv")[0]
    if args.output is not None:
        output = args.output

    shortest.to_csv(output.split(".csv")[0] + "_shortest.csv", index = False)

    r1 = export_to_pyXlinkViewer(shortest, output.split(".csv")[0] + "_shortest.txt")
    r2 = export_to_PAEViewer(output.split(".csv")[0] + "_shortest.csv", output.split(".csv")[0] + "_shortest_PAEViewer.csv", args.threshold)

if __name__ == "__main__":
    main()
