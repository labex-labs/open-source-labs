# Label the Most Uncertain Points

We will add the human labels to the labeled data points and train the model with them.

```python
y_train[uncertainty_index] = y[uncertainty_index]
lp_model.fit(X, y_train)
```


