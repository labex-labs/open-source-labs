# Funktion definieren, um die initialen Mittelwerte zu erhalten

Als nächstes definieren wir eine Funktion `get_initial_means`, die die Stichproben-Daten, die Initialisierungsmethode und den Zufallszustand als Eingaben nimmt und die initialen Mittelwerte zurückgibt.

```python
def get_initial_means(X, init_params, r):
    # Führen Sie ein GaussianMixture mit max_iter=0 aus, um die initialen Mittelwerte auszugeben
    gmm = GaussianMixture(
        n_components=4, init_params=init_params, tol=1e-9, max_iter=0, random_state=r
    ).fit(X)
    return gmm.means_
```
