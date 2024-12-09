import pandas as pd
import os
from openpyxl import load_workbook

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'phone_numbers.xlsx')
output_file_path = os.path.join(script_dir, 'cleaned_phone_numbers.xlsx')
