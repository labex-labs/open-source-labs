# Построение границы решения

В этом шаге мы построим поверхность решения и векторы поддержки. Мы будем использовать модуль DecisionBoundaryDisplay из модуля inspection библиотеки scikit-learn для построения границы решения. Также построим точечный график для тренировочных точек.

```python
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
)

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolors="k")
plt.title("3-Class classification using Support Vector Machine with custom kernel")
plt.axis("tight")
plt.show()
```
