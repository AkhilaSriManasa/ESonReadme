import csv
import os
import sys
import io
import pandas as pd
import matplotlib.pyplot as plt

files = [f for f in os.listdir() if f.startswith("Scores_")]

features = ['C1','C2','C3','C4','C5','C6', 'C7']

characteristics = ['progress_score', 'community_score', 'popularity_score']
for f in files:
    language = f.replace(".csv","").split("_")[1]
    df = pd.read_csv(f)
    for c in characteristics:
        sorted_df = df.sort_values(by=[c], ascending=False)
        # print(max(df[c]))
        for fe in features:
            y = sorted_df[fe]
            x = sorted_df[c].index
            # print(x)
            # print(y)
            plt.scatter(x, y, color = 'g', marker = 'o',label = fe, s= 5)
            heading = 'Distribution of '+fe+' with '+c+ ' for '+language 
            plt.xticks(rotation = 25) 
            plt.xlabel('Score')
            plt.ylabel(fe) 
            custom_y_ticks = [0, 1]
            plt.yticks(custom_y_ticks)
            plt.title(heading, fontsize = 10) 
            plt.grid() 
            # plt.legend() 
            # plt.show() 
            plt.savefig(c+"_"+fe+"_"+language+'.png')
  
