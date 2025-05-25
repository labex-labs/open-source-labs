# Gerar Blobs

O próximo passo é gerar blobs para fazer uma comparação entre MiniBatchKMeans e BIRCH. Usaremos todas as cores fornecidas por padrão pelo matplotlib.

```python
# Gerar centros para os blobs de forma a formar uma grade de 10 x 10.
xx = np.linspace(-22, 22, 10)
yy = np.linspace(-22, 22, 10)
xx, yy = np.meshgrid(xx, yy)
n_centers = np.hstack((np.ravel(xx)[:, np.newaxis], np.ravel(yy)[:, np.newaxis]))

# Gerar blobs para fazer uma comparação entre MiniBatchKMeans e BIRCH.
X, y = make_blobs(n_samples=25000, centers=n_centers, random_state=0)

# Usar todas as cores fornecidas por padrão pelo matplotlib.
colors_ = cycle(colors.cnames.keys())
```
