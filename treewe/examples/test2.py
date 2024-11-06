from sklearn.multioutput import RegressorChain
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(solver='lbfgs')
X, Y = [[1, 0], [0, 1], [1, 1]], [[0, 2], [1, 1], [2, 0]]
chain = RegressorChain(base_estimator=logreg).fit(X, Y)
print(chain.predict(X))