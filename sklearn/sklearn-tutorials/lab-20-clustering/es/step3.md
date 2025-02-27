# Visualizar los datos

Vamos a visualizar los datos generados utilizando un diagrama de dispersión.

```python
# Plot the data points
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```
