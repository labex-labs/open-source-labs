# Splines Periódicas

Demonstramos o uso de splines periódicas utilizando o `SplineTransformer` e especificando manualmente os nós. Ajustamos um modelo de regressão de ridge aos dados de treino e representamos graficamente a função, os pontos de treino e a interpolação usando splines periódicas.

```python
def g(x):
    """Função a ser aproximada por interpolação spline periódica."""
    return np.sin(x) - 0.7 * np.cos(x * 3)


y_train = g(x_train)

# Estender os dados de teste para o futuro:
x_plot_ext = np.linspace(-1, 21, 200)
X_plot_ext = x_plot_ext[:, np.newaxis]

lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(color=["black", "tomato", "teal"])
ax.plot(x_plot_ext, g(x_plot_ext), linewidth=lw, label="verdade fundamental")
ax.scatter(x_train, y_train, label="pontos de treino")

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
