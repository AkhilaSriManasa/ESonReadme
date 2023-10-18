from scipy.stats import ranksums
import numpy as np
from csv import writer
import pandas as pd
import sys
language = sys.argv[1]
file = "Res_"+language+".csv"

df = pd.read_csv(file)


sample1 = pd.DataFrame()
sample2 = pd.DataFrame()


sample1 = df.loc[df['Label'] == 1]
sample2 = df.loc[df['Label'] == 0]
features = ['List','Image','Animation','Video','Table','Github','Links','Project','Inline','Code']
with open("Results/WilcoxonResults"+language+".csv",'a') as csv_file:
	write_csv = writer(csv_file)
	write_csv.writerow(["P-value", "Feature"])
	for feature in features:
		[s,p] = ranksums(sample1[feature], sample2[feature])
		write_csv.writerow([p,feature])
