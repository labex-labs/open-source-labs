# Datensatz generieren

Wir werden einen 3-Klassen-Datensatz mit der Funktion `make_blobs` aus scikit-learn generieren. Wir werden 1000 Stichproben verwenden und die Mittelpunkte der Blobs auf `[-5, 0], [0, 1.5], [5, -1]` setzen. Anschließend werden wir den Datensatz mit einer Transformationsmatrix transformieren, um den Datensatz schwieriger zu klassifizieren.

```python
centers = [[-5, 0], [0, 1.5], [5, -1]]
X, y = make_blobs(n_samples=1000, centers=centers, random_state=40)
transformation = [[0.4, 0.2], [-0.4, 1.2]]
X = np.dot(X, transformation)
```
