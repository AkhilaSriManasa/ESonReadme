import io
import csv
import pandas as pd
from csv import writer
import numpy as np
import re
import sys
import os

file1 = pd.read_csv("Results/RFC.csv", header=None, names=["X","Y"])
file2 = pd.read_csv("Results/RFC_PERM.csv", header=None, names=["X","Y"])

def summary(f1):
    final_data1 = {}
    for row in f1.index:
        if f1['X'][row] == "Language":
            temp_lang = f1['Y'][row] 
            final_data1[f1['Y'][row]] = {}
        if f1['X'][row].startswith("C"):
            final_data1[temp_lang][f1['X'][row]] = round(float(f1['Y'][row]),2)
        if(f1['X'][row]=="Accuracy"):
            final_data1[temp_lang][f1['X'][row]] = round(float(f1['Y'][row]),2)

    col = ["CID"]
    col.append(', '.join(list(final_data1.keys())))
    print(col)
    df1 = pd.DataFrame(final_data1)
    return df1
dfile1 = summary(file1)
dfile2 = summary(file2)
dfile1.to_csv("Results/RFC_summary.csv")
dfile2.to_csv("Results/RFC_PERM_summary.csv")

