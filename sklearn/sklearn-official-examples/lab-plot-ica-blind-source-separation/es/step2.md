# Ajustar los modelos de ICA y PCA

Usaremos FastICA para estimar las fuentes independientes. Luego, calcularemos PCA para comparación.

```python
from sklearn.decomposition import FastICA, PCA

# Calcular ICA
ica = FastICA(n_components=3, whiten="arbitrary-variance")
S_ = ica.fit_transform(X)  # Reconstruir señales
A_ = ica.mixing_  # Obtener la matriz de mezcla estimada

# Podemos `probar` que el modelo de ICA es aplicable revertir la desmezcla.
assert np.allclose(X, np.dot(S_, A_.T) + ica.mean_)

# Para comparación, calcular PCA
pca = PCA(n_components=3)
H = pca.fit_transform(X)  # Reconstruir señales basadas en componentes ortogonales
```
