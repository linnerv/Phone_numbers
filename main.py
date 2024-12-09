import pandas as pd
import os
from openpyxl import load_workbook

script_dir = os.path.dirname(os.path.abspath(file))
file_path = os.path.join(script_dir, 'phone_numbers.xlsx')

df = pd.read_excel(file_path)
df.to_excel(file_path, index=False)