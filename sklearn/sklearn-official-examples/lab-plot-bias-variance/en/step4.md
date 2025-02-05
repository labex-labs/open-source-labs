# Define the Models to Compare

We will define two models to compare: a single decision tree and a bagging ensemble of decision trees.

```python
estimators = [
    ("Tree", DecisionTreeRegressor()),
    ("Bagging(Tree)", BaggingRegressor(DecisionTreeRegressor())),
]
n_estimators = len(estimators)
```
