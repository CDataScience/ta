import pandas as pd
import ta

# Load data from a CSV file downloaded from Yahoo Finance
data = pd.read_csv('path/to/your/csv/file.csv')

# Identify Ascending Triangle pattern
ascending_triangle = ta.patterns.ascendant_triangle(data['High'], data['Low'], data['Close'])
print("Ascending Triangle Pattern:", ascending_triangle)

# Identify Descending Triangle pattern
descending_triangle = ta.patterns.descendant_triangle(data['High'], data['Low'], data['Close'])
print("Descending Triangle Pattern:", descending_triangle)

# Identify Symmetrical Triangle pattern
symmetrical_triangle = ta.patterns.symbols(data['High'], data['Low'], data['Close'], pattern='symmetrical')
print("Symmetrical Triangle Pattern:", symmetrical_triangle)
