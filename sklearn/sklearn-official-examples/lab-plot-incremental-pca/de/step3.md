# Inkrementelle Hauptkomponentenanalyse (IPCA) durchführen

Wir werden die IPCA auf dem Iris-Datensatz durchführen, indem wir eine Instanz der IPCA-Klasse initialisieren und sie auf die Daten anpassen.

```python
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)
```
