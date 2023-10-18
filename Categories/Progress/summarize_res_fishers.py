import io
import csv
import pandas as pd
from csv import writer
import numpy as np
from scipy.stats import hypergeom
from scipy.stats import fisher_exact
import sys
import os

p_less = {}
p_more = {}

files = [file for file in os.listdir('.') if file.startswith("Results/FishersResults_")]

for file in files:
    print(file)
    df = pd.read_csv(file)
    lang = file.split("_")[1].split(".")[0]
    for i in range(0, len(df['CategoryID'])):
        get_category_id = df['CategoryID'][i]
        
        if(df['P-value'][i]<0.05):
            try:
                p_less[str(get_category_id)].append(lang)
            except Exception as e:
                print(f"Failed: {lang}, {get_category_id}")
                
                p_less[str(get_category_id)] = [lang]    
        else:
            try:
                p_more[str(get_category_id)].append(lang)
            except Exception as e:
                print(f"Failed in more : {lang}, {get_category_id}")
                p_more[str(get_category_id)] = [lang]    
print(p_more)
print(p_less)
df1 = pd.DataFrame(columns = ["CID", "PL"])
for j in range(0, len(p_less)):
    df1.at[j, "CID"] = list(p_less.keys())[j]
    df1.at[j, "PL"] = ", ".join(p_less[list(p_less.keys())[j]])
df2 = pd.DataFrame(columns = ["CID", "PM"])
for j in range(0, len(p_more)):
    df2.at[j, "CID"]  = list(p_more.keys())[j]
    df2.at[j, "PM"] = ", ".join(p_more[list(p_more.keys())[j]])
df3 = pd.merge(df1,df2, on="CID", how='outer')

df3.to_csv("Results/Fishers_Summary.csv")
