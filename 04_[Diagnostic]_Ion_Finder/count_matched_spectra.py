from pyteomics import mgf

mass_file = "masses.txt"
mgf_file = "XLpeplib_Beveridge_QEx-HFX_DSS_R1.mgf"

def load_masses(mass_file):
    with open(mass_file) as f:
        return [float(line.strip()) for line in f if line.strip()]
    
def count_masses(mgf_file, masses, tol=0.02):
    counts = {m: 0 for m in masses}

    for spectrum in mgf.read(mgf_file):
        mz_values = spectrum['m/z array']
        for query_mass in masses:
            if any(abs(query_mass - mz) < tol for mz in mz_values):
                counts[query_mass] += 1
    return counts

if __name__ == "__main__":
    masses = load_masses(mass_file)
    counts = count_masses(mgf_file, masses)

    for m, c in counts.items():
        print(f"{m:<12} -> {c}")
