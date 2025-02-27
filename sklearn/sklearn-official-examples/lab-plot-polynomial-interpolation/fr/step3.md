# Interpolation avec des B-splines

Nous utiliserons `SplineTransformer` pour générer des fonctions de base B-spline et ajuster un modèle de régression ridge aux données d'entraînement. Ensuite, nous traçons la fonction, les points d'entraînement et l'interpolation en utilisant les B-splines.

```python
# B-spline avec 4 + 3 - 1 = 6 fonctions de base
model = make_pipeline(SplineTransformer(n_knots=4, degree=3), Ridge(alpha=1e-3))
model.fit(X_train, y_train)

y_plot = model.predict(X_plot)
ax.plot(x_plot, y_plot, label="B-spline")
ax.legend(loc="bas centre")
ax.set_ylim(-20, 10)
plt.show()
```
