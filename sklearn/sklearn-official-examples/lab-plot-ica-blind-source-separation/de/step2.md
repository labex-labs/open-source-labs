# ICA- und PCA-Modelle anpassen

Wir werden FastICA verwenden, um die unabhängigen Quellen zu schätzen. Anschließend berechnen wir PCA zum Vergleich.

```python
from sklearn.decomposition import FastICA, PCA

# ICA berechnen
ica = FastICA(n_components=3, whiten="arbitrary-variance")
S_ = ica.fit_transform(X)  # Signale rekonstruieren
A_ = ica.mixing_  # Geschätzte Mischmatrix erhalten

# Wir können das ICA-Modell durch Rückführung der Entmischung `beweisen`.
assert np.allclose(X, np.dot(S_, A_.T) + ica.mean_)

# Zum Vergleich PCA berechnen
pca = PCA(n_components=3)
H = pca.fit_transform(X)  # Signale basierend auf orthogonalen Komponenten rekonstruieren
```
