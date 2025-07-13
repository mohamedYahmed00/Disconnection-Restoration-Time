import pandas as pd
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Function to clear terminal (cross-platform)
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

# File dialog to select CSV
root = Tk()
root.withdraw()
filename = askopenfilename(title="Select CSV File")
root.destroy()

if not filename:
    print("No file selected.")
    exit(1)

# Read CSV and select columns
df = pd.read_csv(filename, usecols=['Date', 'Inbound', 'Outbound'])
df.fillna(0, inplace=True)
df.loc[df['Outbound'] < 1000, 'Outbound'] = 0

for idx in range(len(df)):
    outbound = df.at[idx, 'Outbound']
    date = df.at[idx, 'Date']
    if outbound == 0:
        print('-', date)
        # Check next row if not at the end
        if idx < len(df) - 1:
            next_outbound = df.at[idx + 1, 'Outbound']
            next_date = df.at[idx + 1, 'Date']
            if outbound != next_outbound:
                print('- Restored', next_date)
