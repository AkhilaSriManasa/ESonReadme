import os
import csv
import pandas as pd
import sys

language = sys.argv[1]

df1 = pd.read_csv("Results/Categories_Spearman_"+language+".csv")

df = pd.DataFrame(columns = ["spearman_coefficient", "Category1", "Category2"])

for each in range(len(df1['spearman_coefficient'])):
	# print(df1.iloc[each]['Hypothesis'])
	if(df1.iloc[each]['spearman_coefficient']>=0.7 or df1.iloc[each]['spearman_coefficient']<=-0.7 ):
		
		s = df1.iloc[each]["spearman_coefficient"]
		f1 = df1.iloc[each]["Category1"]
		f2 = df1.iloc[each]["Category2"]
		
		print(df1.iloc[each]['spearman_coefficient'])
		print(df1.iloc[each]['Category1'])
		print(df1.iloc[each]['Category2'])
		print("_____________________________________________________________________________________")
		df.loc[len(df)] = [s,f1,f2]

# 		print("__________________________________________________________________________________________")

# df.to_csv("Corr_features_"+language+".csv")
df.to_csv("Results/Corr_Categories_"+language+".csv")
list_1 = []

for each in range(len(df['spearman_coefficient'])):
	i = df.iloc[each]['Category1']
	j = df.iloc[each]['Category2']
	for ele in list_1:
		if((i not in ele) or (j not in ele)):
			list_1.append((i,j))
print(list_1)			
