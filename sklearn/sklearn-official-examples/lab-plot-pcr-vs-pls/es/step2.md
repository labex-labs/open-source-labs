# Definir la variable objetivo

Para este ejemplo, definimos la variable objetivo `y` de manera que esté fuertemente correlacionada con una dirección que tiene una baja varianza. Proyectamos `X` sobre el segundo componente y le agregamos algo de ruido.

```python
y = X.dot(pca.components_[1]) + rng.normal(size=n_samples) / 2

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

axes[0].scatter(X.dot(pca.components_[0]), y, alpha=0.3)
axes[0].set(xlabel="Datos proyectados sobre el primer componente PCA", ylabel="y")
axes[1].scatter(X.dot(pca.components_[1]), y, alpha=0.3)
axes[1].set(xlabel="Datos proyectados sobre el segundo componente PCA", ylabel="y")
plt.tight_layout()
plt.show()
```
