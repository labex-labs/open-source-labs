# Visualize the results

Finally, let's visualize the results of our isotonic regression model. We can plot the original data points as scatter points and the predicted values as a line.

```python
import matplotlib.pyplot as plt

# Plot the original data and predicted values
plt.scatter(X, y, c='b', label='Original Data')
plt.plot(X_new, y_pred, c='r', label='Isotonic Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```
