# Modelo de Mistura Gaussiana

Vamos explorar o uso do Modelo de Mistura Gaussiana, que pode lidar com distribuições anisótropas e de variância desigual. No bloco de código a seguir, usamos `GaussianMixture` para agrupar os segundo e terceiro conjuntos de dados.

```python
from sklearn.mixture import GaussianMixture

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

y_pred = GaussianMixture(n_components=3).fit_predict(X_aniso)
ax1.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
ax1.set_title("Blobs Distribuídos Anisotropicamente")

y_pred = GaussianMixture(n_components=3).fit_predict(X_varied)
ax2.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
ax2.set_title("Variância Desigual")

plt.suptitle("Clusters do modelo de mistura gaussiana").set_y(0.95)
plt.show()
```
