import gui
import pandas as pd
import os
import sys
from openpyxl import load_workbook

file = gui.copy_file()
if file != "cancel" and file != False:
    print("file in dir: ", file)

    # === === === === Extract data from file into dataframe === === === ===
    data = pd.read_excel(file)
    df = pd.DataFrame(data)

    # initialise unpaid persons array
    unpaid_persons = []

    # print(df)
    for i in range(len(df)):
        if df.loc[i, "Paid"] == False:
            unpaid_persons.append(df.loc[i])

    print(pd.DataFrame(unpaid_persons))

    
