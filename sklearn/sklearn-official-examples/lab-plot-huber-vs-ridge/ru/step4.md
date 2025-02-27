# Визуализируем набор данных

Теперь мы визуализируем набор данных с использованием matplotlib. Мы построим график значений X по отношению к значениям y.

```python
plt.plot(X, y, "b.")
plt.title("Dataset with Strong Outliers")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
