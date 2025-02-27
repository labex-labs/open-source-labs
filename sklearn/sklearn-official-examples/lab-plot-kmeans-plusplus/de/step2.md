# Initialwerte aus K-Means++ berechnen

Wir werden die Funktion `kmeans_plusplus` der scikit-learn-Bibliothek verwenden, um die Initialwerte aus K-Means++ zu berechnen. Diese Funktion gibt die initialen Clusterzentren zurück, die für die k-means-Gruppierung verwendet werden. Wir werden 4 Cluster mit K-Means++ berechnen.

```python
# Calculate seeds from k-means++
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```
