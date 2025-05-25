# Interpolação com B-Splines

Usaremos `SplineTransformer` para gerar funções de base B-spline e ajustar um modelo de regressão de ridge aos dados de treino. Em seguida, representaremos graficamente a função, os pontos de treino e a interpolação usando B-splines.

```python
# B-spline com 4 + 3 - 1 = 6 funções de base
model = make_pipeline(SplineTransformer(n_knots=4, degree=3), Ridge(alpha=1e-3))
model.fit(X_train, y_train)

y_plot = model.predict(X_plot)
ax.plot(x_plot, y_plot, label="B-spline")
ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
