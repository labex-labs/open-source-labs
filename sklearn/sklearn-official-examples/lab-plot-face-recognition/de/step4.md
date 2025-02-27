# PCA durchführen

```python
n_components = 150

pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
```

Wir führen die Hauptkomponentenanalyse (PCA) durch, um Merkmale aus den Eingabedaten zu extrahieren. Wir setzen die Anzahl der Komponenten auf 150 und trainieren das PCA-Modell mit den Trainingsdaten. Anschließend erhalten wir die Eigenfaces und transformieren die Eingabedaten in Hauptkomponenten.