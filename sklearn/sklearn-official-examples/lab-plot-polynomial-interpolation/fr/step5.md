# Splines périodiques

Nous démontrons l'utilisation de splines périodiques en utilisant `SplineTransformer` et en spécifiant manuellement les noeuds. Nous ajustons un modèle de régression ridge aux données d'entraînement et traçons la fonction, les points d'entraînement et l'interpolation en utilisant des splines périodiques.

```python
def g(x):
    """Fonction à approcher par interpolation de spline périodique."""
    return np.sin(x) - 0.7 * np.cos(x * 3)


y_train = g(x_train)

# Étendre les données de test dans le futur :
x_plot_ext = np.linspace(-1, 21, 200)
X_plot_ext = x_plot_ext[:, np.newaxis]

lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(color=["black", "tomato", "teal"])
ax.plot(x_plot_ext, g(x_plot_ext), linewidth=lw, label="vérité terrain")
ax.scatter(x_train, y_train, label="points d'entraînement")

for transformer, label in [
    (SplineTransformer(degree=3, n_knots=10), "spline"),
    (
        SplineTransformer(
            degree=3,
            knots=np.linspace(0, 2 * np.pi, 10)[:, None],
            extrapolation="periodique",
        ),
        "spline périodique",
    ),
]:
    model = make_pipeline(transformer, Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot_ext = model.predict(X_plot_ext)
    ax.plot(x_plot_ext, y_plot_ext, label=label)

ax.legend()
fig.show()
```
