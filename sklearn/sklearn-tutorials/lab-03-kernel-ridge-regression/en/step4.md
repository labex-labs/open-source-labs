# Visualize the Predicted Function

Once the model is trained, let's visualize the predicted function along with the original data points.

```python
# Generate test data points
X_test = np.linspace(0, 5, 100)[:, None]

# Predict the target values
y_pred = krr.predict(X_test)

# Visualize the data and the predicted function
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_test, y_pred, color='red', label='Predicted Function')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
