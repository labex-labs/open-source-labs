# Построить гиперплоскость разделения с максимальным отступом

Для построения гиперплоскости разделения с максимальным отступом мы будем использовать функцию `DecisionBoundaryDisplay.from_estimator()` из scikit-learn. Эта функция строит функцию решения и векторы поддержки классификатора SVM. Также мы построим векторы поддержки в виде кругов без заливки и с черной обводкой.

```python
from sklearn.inspection import DecisionBoundaryDisplay

# plot the decision function and support vectors
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[-1, 0, 1],
    alpha=0.5,
    linestyles=["--", "-", "--"],
    ax=ax,
)
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
plt.show()
```
