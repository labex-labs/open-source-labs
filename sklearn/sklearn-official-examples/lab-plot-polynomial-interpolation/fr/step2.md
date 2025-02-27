# Interpolation avec des fonctionnalités polynômiales

Nous utiliserons `PolynomialFeatures` pour générer des fonctionnalités polynômiales et ajuster un modèle de régression ridge aux données d'entraînement. Ensuite, nous traçons la fonction, les points d'entraînement et l'interpolation en utilisant les fonctionnalités polynômiales.

```python
# tracé de la fonction
lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(
    color=["black", "teal", "yellowgreen", "gold", "darkorange", "tomato"]
)
ax.plot(x_plot, f(x_plot), linewidth=lw, label="vérité terrain")

# tracé des points d'entraînement
ax.scatter(x_train, y_train, label="points d'entraînement")

# fonctionnalités polynômiales
for degree in [3, 4, 5]:
    model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot = model.predict(X_plot)
    ax.plot(x_plot, y_plot, label=f"degré {degree}")

ax.legend(loc="bas centre")
ax.set_ylim(-20, 10)
plt.show()
```
