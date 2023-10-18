import os
import csv
from csv import writer
import pandas as pd
from sklearn.metrics import make_scorer,accuracy_score
from sklearn.model_selection import GridSearchCV
import sys
from sklearn.model_selection import train_test_split



language = sys.argv[1]
df1 = pd.read_csv("Results/Corr_Categories_"+language+".csv")

list_1 = []
for each in range(len(df1['s'])):
	i = df1.iloc[each]['F1']
	j = df1.iloc[each]['F2']
	flag = 1
	for ele in list_1:
		if(((i not in ele) or (j not in ele)) and flag!=0):
			flag = 1
		else:
			flag = 0
			
	if(flag==1):
		list_1.append([i,j])
# list_1.append(['Github','Image'])
print(list_1)

# Python program to find the common elements
# in two lists
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        return (a_set & b_set)
    else:
        return "No common elements"
          
correlated_features = []  
for lhs in list_1:
	for rhs in list_1:
		if(lhs!=rhs):
			cfeature = ', '.join(common_member(lhs,rhs))
			# S = ', '.join(s)
			print(cfeature)

			if(cfeature not in correlated_features):
				correlated_features.append(cfeature)


		if(len(list_1)==1):
			correlated_features.append(lhs[0])
				
print("Print")
if(len(correlated_features)):
	print(correlated_features[0])
# cf = sys.argv[2]
# correlated_features = cf.split(',')
# correlated_features = sys.argv[2]


df = pd.read_csv("Results/Categories_"+language+".csv")

X=(df[df.columns[1:10]])

for each in correlated_features:
	if(each in X):
		X = X.drop([each], axis = 1)



print(X)

feature_names = ((X.columns))

print(feature_names)



y=df['label']  # Labels


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
