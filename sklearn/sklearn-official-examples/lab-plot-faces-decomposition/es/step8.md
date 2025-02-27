# Componentes de Análisis Factorial - FA

El Análisis Factorial es un método para modelar la varianza en cada dirección del espacio de entrada de manera independiente (ruido heterocedástico), similar a la PCA pero con esta ventaja. Aplicamos FactorAnalysis, que es una implementación del Análisis Factorial en scikit-learn.

```python
# Componentes de Análisis Factorial - FA
fa_estimator = decomposition.FactorAnalysis(n_components=n_components, max_iter=20)
fa_estimator.fit(faces_centered)
plot_gallery("Análisis Factorial (FA)", fa_estimator.components_[:n_components])

# --- Varianza pixel a pixel
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
plt.title("Varianza pixel a pixel a partir de \n Análisis Factorial (FA)", size=16, wrap=True)
plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.03)
plt.show()
```
