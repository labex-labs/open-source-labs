# Splines Periódicas

Demostramos el uso de splines periódicas utilizando el `SplineTransformer` y especificando manualmente los nudos. Ajustamos un modelo de regresión con regularización L2 a los datos de entrenamiento y graficamos la función, los puntos de entrenamiento y la interpolación utilizando splines periódicas.

```python
def g(x):
    """Función a aproximar por interpolación con spline periódica."""
    return np.sin(x) - 0.7 * np.cos(x * 3)


y_train = g(x_train)

# Extender los datos de prueba hacia el futuro:
x_plot_ext = np.linspace(-1, 21, 200)
X_plot_ext = x_plot_ext[:, np.newaxis]

lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(color=["black", "tomato", "teal"])
ax.plot(x_plot_ext, g(x_plot_ext), linewidth=lw, label="verdadero valor")
ax.scatter(x_train, y_train, label="puntos de entrenamiento")

for transformer, label in [
    (SplineTransformer(degree=3, n_knots=10), "spline"),
    (
        SplineTransformer(
            degree=3,
            knots=np.linspace(0, 2 * np.pi, 10)[:, None],
            extrapolation="periodic",
        ),
        "spline periódica",
    ),
]:
    model = make_pipeline(transformer, Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot_ext = model.predict(X_plot_ext)
    ax.plot(x_plot_ext, y_plot_ext, label=label)

ax.legend()
fig.show()
```
