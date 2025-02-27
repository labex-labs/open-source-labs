# Faktorenanalysekomponenten - FA

Die Faktorenanalyse ist eine Methode zur modellierung der Varianz in jeder Richtung des Eingaberaums unabhängig (heteroskedastischer Rauschen), ähnlich wie die PCA, aber mit diesem Vorteil. Wir wenden FactorAnalysis an, was eine Implementierung der Faktorenanalyse in scikit-learn ist.

```python
# Factor Analysis components - FA
fa_estimator = decomposition.FactorAnalysis(n_components=n_components, max_iter=20)
fa_estimator.fit(faces_centered)
plot_gallery("Factor Analysis (FA)", fa_estimator.components_[:n_components])

# --- Pixelweise Varianz
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
plt.title("Pixelweise Varianz aus \n Faktorenanalyse (FA)", size=16, wrap=True)
plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.03)
plt.show()
```
