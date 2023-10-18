import io
import csv
import pandas as pd
from csv import writer
import numpy as np
import sys
import os

n = {}
s = {}
m = {}
l = {}

files = [file for file in os.listdir('.') if file.startswith("Results/CliffsResults_")]
# effect_sizes = ['N', 'S', 'M', 'L']

# print(files)
for file in files:
    print(file)
    df = pd.read_csv(file)
    lang = file.split("_")[1].split(".")[0]
    for i in range(0, len(df['Feature'])):

        get_feature_id = df['Feature'][i]
        # print(get_feature_id)
        if(df['Result'][i]=="negligible"):
            try:
                n[str(get_feature_id)].append(lang)
            except Exception as e:
                print(f"Failed: {lang}, {get_feature_id}")
                
                n[str(get_feature_id)] = [lang]
        if(df['Result'][i]=="small"):
            try:
                s[str(get_feature_id)].append(lang)
            except Exception as e:
                print(f"Failed: {lang}, {get_feature_id}")
                
                s[str(get_feature_id)] = [lang]    
        if(df['Result'][i]=="medium"):
            try:
                m[str(get_feature_id)].append(lang)
            except Exception as e:
                print(f"Failed: {lang}, {get_feature_id}")
                
                m[str(get_feature_id)] = [lang]
        if(df['Result'][i]=="large"):
            try:
                l[str(get_feature_id)].append(lang)
            except Exception as e:
                print(f"Failed: {lang}, {get_feature_id}")
                
                l[str(get_feature_id)] = [lang]    
            
    
print(n)

def dict_df(dict_value, e):
    df1 = pd.DataFrame(columns = ["FID", e])
    for j in range(0, len(dict_value)):
        df1.at[j, "FID"] = list(dict_value.keys())[j]
        df1.at[j, e] = ", ".join(dict_value[list(dict_value.keys())[j]])
    return df1    

dfN = dict_df(n,"N")
dfS = dict_df(s,"S")
dfM = dict_df(m,"M")
dfL = dict_df(l,"L")
dfNS = pd.merge(dfN,dfS, on="FID", how='outer')
dfML = pd.merge(dfM,dfL, on="FID", how='outer') 
df_final = pd.merge(dfNS, dfML, on="FID", how="outer")

df_final.to_csv("Results/Cliffs_Summary.csv")
