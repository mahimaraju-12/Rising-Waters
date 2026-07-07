# Import required libraries

try:
    import numpy as np          # For dealing with high-dimensional data
    import pandas as pd         # To do statistical data analysis
    import matplotlib.pyplot as plt   # For 2D visualization
    import seaborn as sns       # High-end data visualization
except ImportError as e:
    missing_package = str(e).split("'")[1] if "'" in str(e) else str(e)
    print(f"Missing package: {missing_package}. Install it with:")
    print("    python -m pip install numpy pandas matplotlib seaborn")
    raise