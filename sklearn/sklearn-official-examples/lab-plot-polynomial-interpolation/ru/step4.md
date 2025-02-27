# Построение графиков трансформеров

Мы отдельно строим все столбцы обоих трансформеров, чтобы получить более глубокое понимание сгенерированных баз признаков.

```python
fig, axes = plt.subplots(ncols=2, figsize=(16, 5))
pft = PolynomialFeatures(degree=3).fit(X_train)
axes[0].plot(x_plot, pft.transform(X_plot))
axes[0].legend(axes[0].lines, [f"степень {n}" for n in range(4)])
axes[0].set_title("PolynomialFeatures")

splt = SplineTransformer(n_knots=4, degree=3).fit(X_train)
axes[1].plot(x_plot, splt.transform(X_plot))
axes[1].legend(axes[1].lines, [f"сплайн {n}" for n in range(6)])
axes[1].set_title("SplineTransformer")

# строим узлы сплайна
knots = splt.bsplines_[0].t
axes[1].vlines(knots[3:-3], ymin=0, ymax=0.8, linestyles="пунктирный")
plt.show()
```
