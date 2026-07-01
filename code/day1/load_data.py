# load fib-sem data from the .am files

import numpy as np
from pathlib import Path

def load_am_file(filepath):
    """Load Amira .am file and return as numpy array"""
    with open(filepath, 'rb') as f:
        # Skip header until we find the data
        content = f.read()
    return content

# Test: Load the Denoised volume
data_path = Path("../../data/fuel-cell/pore-backs-cv_subtraction-files/pore-backs-cv_subtraction-files/Denoised")
print(f"Looking for data at: {data_path}")
print(f"File exists: {data_path.exists()}")

if data_path.exists():
    print("✓ Found data file")
else:
    print("✗ Data file not found")
