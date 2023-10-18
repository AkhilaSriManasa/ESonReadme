import sys
import csv
import numpy as np
from csv import writer
import pandas as pd
import scipy
from scipy.stats import spearmanr
language = sys.argv[1]

filename1 = "Res_"+language+".csv"
# basis_for_div = "Stars"
# feature = "Links"
with open("Results/Categories_Spearman_"+language+".csv",'w') as csv_file:
	write_csv = writer(csv_file)
	write_csv.writerow(['spearman_coefficient','p-value','Category1','Category2'])
sample1 = pd.read_csv(filename1)
category_list = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']
for c1 in category_list:
	for c2 in category_list:
		if(c1 not in c2):
			print(c1)
			print(c2)
			s,p = spearmanr(sample1[c1],sample1[c2])
			print(s)
			print(p)
			with open("Results/Categories_Spearman_"+language+".csv",'a') as csv_file:
				write_csv = writer(csv_file)
				write_csv.writerow([s,p,c1,c2])

