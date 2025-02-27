# Empirische Kovarianz

Die empirische Kovarianzmatrix ist eine häufig verwendete Methode zur Schätzung der Kovarianzmatrix eines Datensatzes. Sie basiert auf dem Prinzip der Maximum-Likelihood-Schätzung und nimmt an, dass die Beobachtungen unabhängig und identisch verteilt (i.i.d.) sind. Die Funktion `empirical_covariance` im Paket `sklearn.covariance` kann verwendet werden, um die empirische Kovarianzmatrix eines gegebenen Datensatzes zu berechnen.

```python
from sklearn.covariance import empirical_covariance

# Compute the empirical covariance matrix
covariance_matrix = empirical_covariance(data)
```
