# Визуализация данных

Мы будем визуализировать датасет Iris с использованием диаграммы рассеяния. Мы построим график длины чашелистика против ширины чашелистика и покрасим точки в соответствии с их классом.

```python
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Длина чашелистика")
plt.ylabel("Ширина чашелистика")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
```
