# Fit the Unweighted Model

We fit an unweighted model using the SGDClassifier algorithm from the scikit-learn library. We then plot the decision function of the unweighted model.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
no_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["solid"])
```


