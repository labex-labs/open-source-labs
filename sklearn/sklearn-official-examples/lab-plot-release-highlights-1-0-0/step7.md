# Evaluate the Quantile Regression Model

Let's evaluate the performance of the quantile regression model on the testing data.

```python
y_pred_quantile = quantile_model.predict(X_test)

plt.scatter(y_test, y_pred_quantile)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()
```
