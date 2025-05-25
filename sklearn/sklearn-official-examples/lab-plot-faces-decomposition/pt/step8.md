# Componentes da Análise Fatorial - FA

A Análise Fatorial é um método para modelar a variância em cada direção do espaço de entrada de forma independente (ruído heterocedástico), semelhante à PCA, mas com esta vantagem. Aplicamos o FactorAnalysis, que é uma implementação da Análise Fatorial no scikit-learn.

```python
# Componentes da Análise Fatorial - FA
fa_estimator = decomposition.FactorAnalysis(n_components=n_components, max_iter=20)
fa_estimator.fit(faces_centered)
plot_gallery("Análise Fatorial (FA)", fa_estimator.components_[:n_components])

# --- Variância pixel a pixel
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
plt.title("Variância pixel a pixel a partir de \n Análise Fatorial (FA)", size=16, wrap=True)
plt.colorbar(orientation="horizontal", shrink=0.8, pad=0.03)
plt.show()
```
