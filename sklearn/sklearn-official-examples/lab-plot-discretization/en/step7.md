# Train a Decision Tree Model

In this step, we will train a decision tree model on the original dataset.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X, y)
```
