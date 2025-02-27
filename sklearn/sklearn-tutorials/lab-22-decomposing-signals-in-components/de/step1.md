# Hauptkomponentenanalyse (PCA)

#### Exakte PCA und probabilistische Interpretation

Die Hauptkomponentenanalyse (PCA) wird verwendet, um einen multivariate Datensatz in eine Reihe aufeinanderfolgender orthogonaler Komponenten zu zerlegen, die die maximale Varianz erklären. Die PCA kann mit der Klasse `PCA` aus scikit-learn implementiert werden. Die `fit`-Methode wird verwendet, um die Komponenten zu lernen, und die `transform`-Methode kann verwendet werden, um neue Daten auf diese Komponenten zu projizieren.

```python
from sklearn.decomposition import PCA

# Erstellen eines PCA-Objekts mit n_components als Anzahl der gewünschten Komponenten
pca = PCA(n_components=2)

# Anpassen des PCA-Modells an die Daten
pca.fit(data)

# Transformation der Daten, indem sie auf die gelernten Komponenten projiziert werden
transformed_data = pca.transform(data)
```
