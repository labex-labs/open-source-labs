# Evaluate the Linear Regression Model

Now, let's evaluate the performance of the linear regression model on the testing data.

```python
y_pred = model.predict(X_test)

plt.scatter(y_test, y_pred)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()
```
