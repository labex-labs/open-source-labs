# Train a Decision Tree Model on the Discretized Dataset

In this step, we will train a decision tree model on the discretized dataset.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X_binned, y)
```


