# Interpolación con B-Spline

Usaremos `SplineTransformer` para generar funciones de base B-spline y ajustar un modelo de regresión con regularización L2 a los datos de entrenamiento. Luego graficaremos la función, los puntos de entrenamiento y la interpolación utilizando B-splines.

```python
# B-spline con 4 + 3 - 1 = 6 funciones de base
model = make_pipeline(SplineTransformer(n_knots=4, degree=3), Ridge(alpha=1e-3))
model.fit(X_train, y_train)

y_plot = model.predict(X_plot)
ax.plot(x_plot, y_plot, label="B-spline")
ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
