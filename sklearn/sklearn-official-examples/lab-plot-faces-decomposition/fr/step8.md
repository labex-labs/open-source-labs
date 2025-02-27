# Composantes d'Analyse en Facteurs - FA

L'Analyse en Facteurs est une méthode pour modéliser la variance dans chaque direction de l'espace d'entrée indépendamment (bruit hétéroscédastique), similaire à la PCA mais avec cet avantage. Nous appliquons FactorAnalysis, qui est une implémentation de l'Analyse en Facteurs dans scikit-learn.

```python
# Composantes d'Analyse en Facteurs - FA
fa_estimator = decomposition.FactorAnalysis(n_components=n_components, max_iter=20)
fa_estimator.fit(faces_centered)
plot_gallery("Analyse en Facteurs (FA)", fa_estimator.components_[:n_components])

# --- Variance pixel par pixel
plt.figure(figsize=(3.2, 3.6), facecolor="white", tight_layout=True)
vec = fa_estimator.noise_variance_
vmax = max(vec.max(), -vec.min())
plt.imshow(
    vec.reshape(image_shape),
    cmap=plt.cm.gray,
    interpolation="nearest",
    vmin=-vmax,
    vmax=vmax,
)
plt.axis("off")
plt.title("Variance pixel par pixel à partir de \n l'Analyse en Facteurs (FA)", size=16, wrap=True)
plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.03)
plt.show()
```
