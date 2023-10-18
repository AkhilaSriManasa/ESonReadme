import sys
import csv
import numpy as np
from csv import writer
import pandas as pd
import scipy
from scipy.stats import spearmanr
language = sys.argv[1]
filename1 = "Features_"+language+".csv"

with open("Results/Features_Spearman_"+language+".csv",'w') as csv_file:
	write_csv = writer(csv_file)
	write_csv.writerow(['S','P','F1','F2'])
sample1 = pd.read_csv(filename1)
features_list = sample1[sample1.columns[1:11]]
print(features_list)

for f1 in features_list:
	for f2 in features_list:
		if(f1 not in f2):
			print(f1)
			print(f2)
			s,p = spearmanr(sample1[f1],sample1[f2])
			print(s)
			print(p)
			with open("Results/Features_Spearman_"+language+".csv",'a') as csv_file:
				write_csv = writer(csv_file)
				write_csv.writerow([s,p,f1,f2])
