# Predict using the model

After fitting the model, we can use it to make predictions on new data. Let's create a new array `X_new` and predict the corresponding target values.

```python
# Create new data for prediction
X_new = np.linspace(0, 1, 100)
y_pred = ir.predict(X_new)
```
