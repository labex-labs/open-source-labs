# Verwende die PCA, um den Datensatz zu projizieren

Die PCA wird verwendet, um den Datensatz in einen neuen Raum zu projizieren, in dem die meiste ursprüngliche Variation erhalten bleibt.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_test_pca = pca.fit(X_train).transform(X_test)
```
