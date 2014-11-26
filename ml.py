from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
import numpy as np

x = np.random.randn(1,50)[0]
Y = x + np.random.rand(1,50)[0]
y = Y.reshape(len(Y),)
print x
print y
"""
scores = []
for t in xrange(40):
    num_trees = t+1
    clf = RandomForestClassifier(n_estimators=num_trees)
    score = cross_val_score(clf,x,y,cv=10,scoring='f1')
    scores.append(np.mean(score))

plt.scatter(np.arange(len(scores))+1,scores)
plt.title("Scores versus Num Trees")
plt.xlabel("Num Trees")
plt.ylabel("Scores")
plt.show()
"""
#convert volcano data from 0 and 1 to indicate if it it exploded in that month or not - turn it into a classification problem

perc_explosions = np.sum(y)/float(len(y))
"""
plt.scatter(np.arange(len(scores))+1,scores)
plt.axhline(y=perc_explosions,color='r')
plt.title("Scores versus Num Trees")
plt.xlabel("Num Trees")
plt.ylabel("Scores")
plt.show()
"""

clf = RandomForestClassifier(n_estimators=15)
clf = clf.fit(x,y)
prob = clf.predict_proba(x)
prop_app = np.apply_along_axis(lambda x: x>.03,1,prob).astype(int)

assert((prop_app[:,1]==clf.predict(X)).all())

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
