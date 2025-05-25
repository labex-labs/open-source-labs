# Ajustar Modelos ICA e PCA

Usaremos o FastICA para estimar as fontes independentes. Em seguida, computaremos a PCA para comparação.

```python
from sklearn.decomposition import FastICA, PCA

# Computar ICA
ica = FastICA(n_components=3, whiten="arbitrary-variance")
S_ = ica.fit_transform(X)  # Reconstruir sinais
A_ = ica.mixing_  # Obter a matriz de mistura estimada

# Podemos "provar" que o modelo ICA se aplica invertendo a desmistura.
assert np.allclose(X, np.dot(S_, A_.T) + ica.mean_)

# Para comparação, computar PCA
pca = PCA(n_components=3)
H = pca.fit_transform(X)  # Reconstruir sinais com base em componentes ortogonais
```
