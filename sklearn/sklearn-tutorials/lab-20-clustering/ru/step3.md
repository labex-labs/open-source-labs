# Визуализируем данные

Давайте визуализируем сгенерированные данные с помощью точечного графика.

```python
# Plot the data points
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```
