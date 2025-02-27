# Gaussian Mixture Model anpassen

Wir werden nun ein GMM an den Datensatz mit der GaussianMixture-Klasse aus scikit-learn anpassen. Wir werden die Anzahl der Komponenten auf 2 und den Kovarianztyp auf "vollständig" setzen.

```python
# passe ein Gaussian Mixture Model mit zwei Komponenten an
clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)
```
