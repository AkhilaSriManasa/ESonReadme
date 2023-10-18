import os
import csv
from csv import writer
import pandas as pd
from sklearn.metrics import make_scorer,accuracy_score
from sklearn.model_selection import GridSearchCV
import sys
from sklearn.model_selection import train_test_split

language = sys.argv[1]
df1 = pd.read_csv("Results/Corr_Features_"+language+".csv")

list_1hs = []
list_rhs = []
list_pair = []
# dict_pair = dictionary()
for each in range(len(df1['spearman-coeffiecient'])):
	i = df1.iloc[each]['Feature1']
	j = df1.iloc[each]['Feature2']
	list_1hs.append(i)
	list_rhs.append(j)
	list_pair.append((i,j))
	# print(list_pair)
frequency_feature = {}
for each in list_1hs:
	if(each in frequency_feature):
		frequency_feature[each] += 1
	else:
		frequency_feature[each] = 1
sorted_features = (dict(sorted(frequency_feature.items(), key=lambda item: item[1], reverse=True)))		
print(sorted_features)
top_key_list = []
top_key_list.append(list(sorted_features.keys())[0])
for each in list_pair:
	i = each[0]
	j = each[1]
	if(i in top_key_list or j in top_key_list):
		print("matched")
	else:
		if(sorted_features[i]>sorted_features[j]):
			top_key_list.append(i)
		if(sorted_features[j]>sorted_features[i]):
			top_key_list.append(j)
		else:
			top_key_list.append(i)
print(top_key_list)			
to_delete = set(list_1hs) -set(top_key_list)



df = pd.read_csv("Res_"+language+".csv")

X=(df[df.columns[1:11]])

for each in to_delete:
	if(each in X):
		X = X.drop([each], axis = 1)

print(X)

feature_names = ((X.columns))
print(feature_names)



y=df['Label']  # Labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=1000, bootstrap = True, oob_score=True,max_depth=2)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

from sklearn import metrics
accuracy = metrics.accuracy_score(y_test, y_pred)
# Model Accuracy, how often is the classifier correct?
print("Language",language)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("score:",clf.score(X_train,y_train))
print("oob_score",clf.oob_score_)


import pandas as pd
feature_imp = pd.Series(clf.feature_importances_,index=feature_names).sort_values(ascending=False)
print(feature_imp)

from sklearn.inspection import permutation_importance
pm = permutation_importance(clf,X_test,y_test)
print("PERM")
sort = pm.importances_mean.argsort()
for e in sort:
	print(feature_names[e]+"___"+str(pm.importances_mean[e]))
# print(pm.importances_mean.argsort())
with open("Results/RFC.csv",'a') as csv_file:
	write_csv = writer(csv_file)
	write_csv.writerow(["Language",language])
	write_csv.writerow(["Accuracy",accuracy])
	write_csv.writerow(['oob_score',clf.oob_score_])
	for i in range(len(feature_imp.index)):
		write_csv.writerow([feature_imp.index[i], feature_imp[i]])

with open("Results/RFC_PERM.csv",'a') as csv_file:
	write_csv = writer(csv_file)
	write_csv.writerow(["Language",language])
	write_csv.writerow(["Accuracy",accuracy])
	write_csv.writerow(['oob_score',clf.oob_score_])
	for e in sort:
		write_csv.writerow([feature_names[e],(pm.importances_mean[e])])
