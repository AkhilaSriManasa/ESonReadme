import os
import csv
import pandas as pd
import sys

language = sys.argv[1]

df1 = pd.read_csv("Results/Features_Spearman_"+language+".csv")

df = pd.DataFrame(columns = ["spearman-coeffiecient", "Feature1", "Feature2"])

for each in range(len(df1["spearman-coeffiecient"])):
	# print(df1.iloc[each]['Hypothesis'])
	if(df1.iloc[each]['spearman-coeffiecient']>=0.7 or df1.iloc[each]['spearman-coeffiecient']<=-0.7 ):
		
		s = df1.iloc[each]["spearman-coeffiecient"]
		f1 = df1.iloc[each]["Feature1"]
		f2 = df1.iloc[each]["Feature2"]
		
		print(df1.iloc[each]['spearman-coeffiecient'])
		print(df1.iloc[each]['Feature1'])
		print(df1.iloc[each]['Feature2'])
		print("_____________________________________________________________________________________")
		df.loc[len(df)] = [s,f1,f2]

# 		print("__________________________________________________________________________________________")

# df.to_csv("Corr_features_"+language+".csv")
df.to_csv("Results/Corr_Features_"+language+".csv")
list_1 = []

for each in range(len(df['spearman-coeffiecient'])):
	i = df.iloc[each]['Feature1']
	j = df.iloc[each]['Feature2']
	for ele in list_1:
		if((i not in ele) or (j not in ele)):
			list_1.append((i,j))
print(list_1)			
