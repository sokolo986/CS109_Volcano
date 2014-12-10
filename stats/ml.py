from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from sklearn import cross_validation
import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd

#data is entire matrix with x and y
#if isRegressor, assumes regression otherwise classification
def feature_importance (data,isRegressor,n_estimators=50,test_estimators=False):

	n,m 	= np.shape(data)
	X 		= np.asarray(data.ix[:,0:m-1])
	y 		= np.asarray(data.ix[:,m-1])
	X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size = .2)

	if test_estimators:
		scores = []
		trees = np.arange(1,70)
		if isRegressor:
			for t in trees:
				clf = RandomForestRegressor(n_estimators=t)
				clf.fit(X_train,y_train)
				y_hat = clf.predict(X_test)
				#score = clf.score(X,y)
				mse = np.mean((y_hat-y_test)**2)
				scores.append(mse)
		else:
			for t in trees:
				clf = RandomForestClassifier(n_estimators=t)
				clf.fit(X_train,y_train)
				#prob = clf.predict_proba(x)
				score = cross_val_score(clf,X_test,y_test,cv=10,scoring='f1')
				scores.append(score)

		#plot
		plt.scatter(trees,scores)
		plt.title("Scores versus Num Trees")
		plt.xlabel("Num Trees")
		plt.ylabel("Scores")
		plt.show()

		print "\nMax:",np.max(scores),"achieved by",trees[np.argmax(scores)],"trees","\nMin score",np.min(scores),"achieved by",trees[np.argmin(scores)],"trees"

	if isRegressor:
		clf = RandomForestRegressor(n_estimators=n_estimators)
		clf.fit(X_train,y_train)
	else:
		clf = RandomForestClassifier(n_estimators=n_estimators)
		clf.fit(X_train,y_train)
	return clf.feature_importances_

if __name__ == '__main__':

	data 	= pd.io.parsers.read_csv('diamonds.csv',sep=',',header=True)

	feature_imp = feature_importance(data,True,n_estimators=60,test_estimators=False)

	print "Feature Importance:",feature_imp
	

