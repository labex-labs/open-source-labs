# Berechnung des Hauptsingulärvektors mit Randomized SVD

Wir werden die Hauptsingulärvektoren mit der in scikit-learn implementierten randomized_svd-Methode berechnen.

```python
from sklearn.decomposition import randomized_svd

print("Berechne die Hauptsingulärvektoren mit randomized_svd")
U, s, V = randomized_svd(X, 5, n_iter=3)
```
