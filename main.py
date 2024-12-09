import pandas as pd
import os
from openpyxl import load_workbook

def process_row(row):
    s = row['phone_number']
    s_new = ''.join(filter(str.isdigit, str(s)))
    row['phone_number'] = s_new
    return row

