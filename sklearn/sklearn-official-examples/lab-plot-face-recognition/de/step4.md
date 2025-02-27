# Hauptkomponentenanalyse (PCA) durchführen

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

Wir führen eine Hauptkomponentenanalyse (Principal Component Analysis, PCA) durch, um Merkmale aus den Eingabedaten zu extrahieren. Wir setzen die Anzahl der Komponenten auf 150 und passen das PCA-Modell an die Trainingsdaten an. Anschließend erhalten wir die Eigenfaces (Eigengesichter) und transformieren die Eingabedaten in Hauptkomponenten.
