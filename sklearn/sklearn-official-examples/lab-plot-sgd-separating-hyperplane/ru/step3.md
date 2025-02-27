# Построим разделяющую гиперплоскость с максимальным отступом

Наконец, мы можем построить разделяющую гиперплоскость с максимальным отступом, которую мы получили с использованием алгоритма SVM с SGD. Мы создадим сетку точек с использованием `np.meshgrid`, а затем вычислим функцию решения для каждой точки на сетке с использованием метода `decision_function` модели SVM. Затем мы построим границу решения с использованием `plt.contour`, а точки данных - с использованием `plt.scatter`.

```python
# plot the line, the points, and the nearest vectors to the plane
xx = np.linspace(-1, 5, 10)
yy = np.linspace(-1, 5, 10)

X1, X2 = np.meshgrid(xx, yy)
Z = np.empty(X1.shape)
for (i, j), val in np.ndenumerate(X1):
    x1 = val
    x2 = X2[i, j]
    p = clf.decision_function([[x1, x2]])
    Z[i, j] = p[0]
levels = [-1.0, 0.0, 1.0]
linestyles = ["dashed", "solid", "dashed"]
colors = "k"
plt.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolor="black", s=20)

plt.axis("tight")
plt.show()
```
