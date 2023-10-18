import io
import csv
import pandas as pd
from csv import writer
import numpy as np
import sys
import os

p_less = {}
p_more = {}

files = [file for file in os.listdir('.') if file.startswith("Results/WilcoxonResults")]
# print(files)
for file in files:
    print(file)
    df = pd.read_csv(file)
    lang = file.split("Results")[1].split(".")[0]
    for i in range(0, len(df.iloc[:, 1])):

        get_feature_id = df.iloc[:, 1][i]
        # print(get_feature_id)
        if(df.iloc[:, 0][i]<0.05):
            try:
                p_less[str(get_feature_id)].append(lang)
            except Exception as e:
                print(f"Failed: {lang}, {get_feature_id}")
                
                p_less[str(get_feature_id)] = [lang]    
        else:
            try:
                p_more[str(get_feature_id)].append(lang)
            except Exception as e:
                print(f"Failed in more : {lang}, {get_feature_id}")
                p_more[str(get_feature_id)] = [lang]    
print(p_more)
print(p_less)
df1 = pd.DataFrame(columns = ["FID", "PL"])
for j in range(0, len(p_less)):
    df1.at[j, "FID"] = list(p_less.keys())[j]
    df1.at[j, "PL"] = ", ".join(p_less[list(p_less.keys())[j]])
df2 = pd.DataFrame(columns = ["FID", "PM"])
for j in range(0, len(p_more)):
    df2.at[j, "FID"]  = list(p_more.keys())[j]
    df2.at[j, "PM"] = ", ".join(p_more[list(p_more.keys())[j]])
df3 = pd.merge(df1,df2, on="FID", how='outer')

df3.to_csv("Results/Wilcoxon_Summary.csv")
