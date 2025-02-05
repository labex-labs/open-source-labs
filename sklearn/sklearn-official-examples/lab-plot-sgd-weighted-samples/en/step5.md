# Fit the Weighted Model

We fit a weighted model using the same algorithm as in Step 4, but this time we pass the sample_weight argument to the fit method. We then plot the decision function of the weighted model.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
samples_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["dashed"])
```
