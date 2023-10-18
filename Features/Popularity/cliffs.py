from cliffs_delta import cliffs_delta

import sys
import csv
import numpy as np
from csv import writer
import pandas as pd
language = sys.argv[1]
file = "Features_"+language+".csv"
df = pd.read_csv(file)
sample1 = df.loc[df['Rank_real'] >= 100]
sample2 = df.loc[df['Rank_real'] < 100]
for feature in sample1:
	d, res = cliffs_delta(sample1[feature], sample2[feature])
	with open("Results/CliffsResults_"+language+".csv",'a') as csv_file:
		write_csv = writer(csv_file)
		write_csv.writerow([d,res,feature])

