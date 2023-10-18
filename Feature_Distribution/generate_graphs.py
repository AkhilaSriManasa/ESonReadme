import csv
import os
import sys
import io
import pandas as pd
import matplotlib.pyplot as plt

files = [f for f in os.listdir() if f.startswith("Scores_")]

features = ['List', 'Image','Animation','Video','Table',	'Github',	'Links',	'Project'	,'Inline',	'Code']
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
            plt.scatter(x, y, color = 'g', marker = 'o',label = fe, s= 2)
            heading = 'Distribution of '+fe+' with '+c+ ' for '+language 
            plt.xticks(rotation = 25) 
            plt.xlabel('Score')
            plt.ylabel(fe) 
            plt.title(heading, fontsize = 10) 
            plt.grid() 
            # plt.legend() 
            # plt.show() 
            plt.savefig(c+"_"+fe+"_"+language+'.png')
  
