# Erzeugen von Beispiel-Daten

Als nächstes erzeugen wir einige Beispiel-Daten, mit denen wir arbeiten können. Wir verwenden die Funktion `make_blobs` aus dem Modul `sklearn.datasets`, um einen synthetischen Datensatz mit Clustern zu erstellen.

```python
# Generate sample data
X, y = make_blobs(n_samples=100, centers=4, random_state=0, cluster_std=1.0)
```
