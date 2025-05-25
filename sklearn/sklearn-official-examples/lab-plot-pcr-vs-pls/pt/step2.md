# Definir o Alvo

Para este exemplo, definimos o alvo `y` de forma que esteja fortemente correlacionado com uma direção que apresenta uma pequena variância. Projetamos `X` no segundo componente e adicionamos algum ruído a ele.

```python
y = X.dot(pca.components_[1]) + rng.normal(size=n_samples) / 2

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

axes[0].scatter(X.dot(pca.components_[0]), y, alpha=0.3)
axes[0].set(xlabel="Dados projetados no primeiro componente PCA", ylabel="y")
axes[1].scatter(X.dot(pca.components_[1]), y, alpha=0.3)
axes[1].set(xlabel="Dados projetados no segundo componente PCA", ylabel="y")
plt.tight_layout()
plt.show()
```
