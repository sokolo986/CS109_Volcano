from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score

y = Y.values.reshape(len(Y),)
scores = []

for t in xrange(40):
    num_trees = t+1
    clf = RandomForestClassifier(n_estimators=num_trees)
    score = cross_val_score(clf,x,y,cv=10)
    scores.append(np.mean(score))

plt.scatter(np.arange(len(scores))+1,scores)
plt.title("Scores versus Num Trees")
plt.xlabel("Num Trees")
plt.ylabel("Scores")
plt.show()


bad_wines = 1-np.sum(y)/float(len(y))
print "Percent of 'bad wines':",1-(np.sum(y)/float(len(y)))

plt.scatter(np.arange(len(scores))+1,scores)
plt.axhline(y=bad_wines,color='r')
plt.title("Scores versus Num Trees")
plt.xlabel("Num Trees")
plt.ylabel("Scores")
plt.show()

s=[]
for t in xrange(40):
    num_trees = t+1
    clf = RandomForestClassifier(n_estimators=num_trees)
    score = cross_val_score(clf,x,y,cv=10,scoring='f1')
    s.append(np.max(score))

plt.scatter(np.arange(len(s))+1,s)
plt.title ("Scores versus Num Trees")
plt.xlabel("Num Trees")
plt.ylabel("Scores")
plt.show()

clf = RandomForestClassifier(n_estimators=15)
clf = clf.fit(x,y)
prob = clf.predict_proba(x)
prop_app = np.apply_along_axis(lambda x: x>.5,1,prob).astype(int)

assert((prop_app[:,1]==clf.predict(X)).all())

"""
cutoff_predict(clf, X, cutoff)

Inputs:
clf: a **trained** classifier object
X: a 2D numpy array of features
cutoff: a float giving the cutoff value used to convert
        predicted probabilities into a 0/1 prediction.

Output:
a numpy array of 0/1 predictions.
"""
def cutoff_predict(clf,X,cutoff):
    assert(cutoff<=1 and cutoff>=0)
    prob = clf.predict_proba(X)
    return np.apply_along_axis(lambda x: x>cutoff,1,prob)[:,1].astype(int)


def custom_f1(cutoff):
    def f1_cutoff(clf, X, y):
        ypred = cutoff_predict(clf, X, cutoff)
        return sklearn.metrics.f1_score(y, ypred)      
    return f1_cutoff

cs=[]
for c in np.arange(.1,.9,.1):
    cs.append(custom_f1(c)(clf,x,y))

print "Cutoff Scores:",cs

plt.boxplot(np.arange(.1,.9,.1),cs)
plt.title("F1 scores for Various Cutoff Values")
plt.xlabel("Cutoff")
plt.ylabel("F1 score")
plt.show()