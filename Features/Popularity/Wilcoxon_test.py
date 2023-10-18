from scipy.stats import ranksums
import numpy as np
from csv import writer
import pandas as pd
import sys
language = sys.argv[1]
file = "Features_"+language+".csv"

df = pd.read_csv(file)


sample1 = pd.DataFrame()
sample2 = pd.DataFrame()


sample1 = df.loc[df['Rank_real'] >= 100]
sample2 = df.loc[df['Rank_real'] < 100]

for feature in sample1:
	[s,p] = ranksums(sample1[feature], sample2[feature])
	with open("Results/WilcoxonResults"+language+".csv",'a') as csv_file:
		write_csv = writer(csv_file)
		write_csv.writerow([p,feature])
