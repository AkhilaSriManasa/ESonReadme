import os
import csv
import pandas as pd
import sys
from sklearn.cluster import KMeans
import numpy as np
import pickle
import math

language = sys.argv[1]

# df1 = pd.read_csv("Categories/old/Refined_"+language+".csv")
df3 = pd.read_csv("Scores_"+language+".csv")

# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()

def add_label(attr):
    kmeans = KMeans(n_clusters=2)
    for i in range(len(df3[attr])):
        print(round(df3[attr][i],4))
        df3[attr][i] = round(df3[attr][i],4)
        if(df3[attr][i]==0):
            df3[attr][i]= df3[attr].nsmallest(2).iloc[-1]    
    # print(np.log(df3[attr]))  
    # df3[attr] = scaler.fit_transform(df3[attr])      
    kmeans.fit((df3[attr]).values.reshape(-1,1))
    print(kmeans.cluster_centers_)
    return kmeans.labels_ 		


cluster_map = pd.DataFrame()
cluster_map = df3
cluster_map['prg_Label'] = add_label('progress_score')
cluster_map['comm_Label'] = add_label('community_score')


cluster_map.to_csv('Res_'+language+'.csv',index=False)


print("done")


