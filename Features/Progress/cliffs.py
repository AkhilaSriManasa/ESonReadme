from cliffs_delta import cliffs_delta

import sys
import csv
import numpy as np
from csv import writer
import pandas as pd
language = sys.argv[1]

file = "Res_"+language+".csv"

df = pd.read_csv(file)


sample1 = df.loc[df['Label'] == 1]
sample2 = df.loc[df['Label'] == 0]
features = ['List','Image','Animation','Video','Table','Github','Links','Project','Inline','Code']
with open("Results/CliffsResults_"+language+".csv",'a') as csv_file:
	write_csv = writer(csv_file)
	write_csv.writerow(["D_value", "Result", "Feature"])
	for feature in features:
		d, res = cliffs_delta(sample1[feature], sample2[feature])
		write_csv.writerow([d,res,feature])

