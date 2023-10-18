import io
import csv
import pandas as pd
from csv import writer
import numpy as np
from scipy.stats import hypergeom
from scipy.stats import fisher_exact
import sys

language = sys.argv[1]

file = "Categories_"+language+".csv"
df = pd.read_csv(file)


sample1 = pd.DataFrame()
sample2 = pd.DataFrame()


df["section_codes_in_file"] = df.where(df[df.columns[1:10]] == 0, 
                                  other=df[df.columns[1:10]].apply(lambda x: x.name), 
                                  axis=1).where(df[df.columns[1:10]] != 0, 
                                                other="").apply(lambda row: ''.join(row.values), axis=1)

sample1 = df.loc[df['Rank_real'] >= 100]
sample2 = df.loc[df['Rank_real'] < 100]


target = sample1['section_codes_in_file']

target_1 = sample2['section_codes_in_file']


for i in range(0,9):
	present_1 = 0
	notpresent_1 = 0
	np_present_1 = 0
	np_notpresent_1 = 0
	for each in target:
		print(each)
		if(each == 'nan'):
			each = '2'
		if(type(each)!=float):
			if(str(i) in each):
				present_1 = present_1 + 1
			else:
				notpresent_1 = notpresent_1 + 1
	for each in target_1:
		if(type(each)!=float):
			if(str(i) in each):
				np_present_1 = np_present_1 + 1
			else:
				np_notpresent_1 = np_notpresent_1 + 1			

	print("present :"+str(present_1))
	print("not present :"+str(notpresent_1))
	print("Non popular")
	print("present :"+str(np_present_1))
	print("not present :"+str(np_notpresent_1))
	table = np.array([[present_1, notpresent_1], [np_present_1, np_notpresent_1]])
	M = table.sum()
	n = table[0].sum()
	N = table[:, 0].sum()
	oddsr, p = fisher_exact(table)
	print(p)
	with open("Results/FishersResults_"+language+".csv",'a') as csv_file:
		write_csv = writer(csv_file)
		write_csv.writerow([p,i])

