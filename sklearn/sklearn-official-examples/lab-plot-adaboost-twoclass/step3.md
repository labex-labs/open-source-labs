# Create and fit an AdaBoosted decision tree

In this step, we will create an AdaBoosted decision tree using the `AdaBoostClassifier` class from the `sklearn.ensemble` module. We will use the decision tree as the base estimator and set the `max_depth` parameter to 1. We will also set the `algorithm` parameter to "SAMME" and the `n_estimators` parameter to 200. Finally, we will fit the classifier to the dataset.

```python
bdt = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200
)

bdt.fit(X, y)
```


