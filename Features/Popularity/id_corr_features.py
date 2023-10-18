import os
import csv
import pandas as pd
import sys

language = sys.argv[1]

df1 = pd.read_csv("Results/Features_Spearman_"+language+".csv")

df = pd.DataFrame(columns = ["s", "F1", "F2"])

for each in range(len(df1['S'])):
	# print(df1.iloc[each]['Hypothesis'])
	if(df1.iloc[each]['S']>=0.7 or df1.iloc[each]['S']<=-0.7 ):
		# df.append(df1.iloc[each], ignore_index = True)
		# l = df1.iloc[each]["Language"]
		s = df1.iloc[each]["S"]
		f1 = df1.iloc[each]["F1"]
		f2 = df1.iloc[each]["F2"]
		# print(df1.iloc[each]['Language'])
		print(df1.iloc[each]['S'])
		print(df1.iloc[each]['F1'])
		print(df1.iloc[each]['F2'])
		print("_____________________________________________________________________________________")
		df.loc[len(df)] = [s,f1,f2]

df.to_csv("Results/Corr_Features_"+language+".csv")
			
