from pathlib import Path
import pandas as pd

def load_laptop_data():
    try:
        base_dir = Path(__file__).resolve().parent.parent  # Goes up to 'Project'
        file_path = base_dir / 'data' / 'laptops.csv'
        laptops_df = pd.read_csv(file_path)
        laptops_df.columns = laptops_df.columns.str.strip()
        return laptops_df
    except FileNotFoundError:
        raise FileNotFoundError(f"Laptop data file not found at: {file_path}")

def load_energy_data():
    try:
        base_dir = Path(__file__).resolve().parent.parent
        file_path = base_dir / 'data' / 'energy_truncated.csv'
        energy_df = pd.read_csv(file_path)
        energy_df.columns = energy_df.columns.str.strip()
        return energy_df
    except FileNotFoundError:
        raise FileNotFoundError(f"Energy data file not found at: {file_path}")

if __name__ == "__main__":
    laptops_df = load_laptop_data()
    energy_df = load_energy_data()

    print(laptops_df.head())
    print(energy_df.head())
