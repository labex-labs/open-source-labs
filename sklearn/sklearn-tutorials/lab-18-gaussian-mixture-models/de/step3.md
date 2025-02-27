# Ein Gaussian Mixture Model anpassen

Jetzt können wir ein Gaussian Mixture Model an unsere Daten anpassen, indem wir die `GaussianMixture`-Klasse aus dem `sklearn.mixture`-Modul verwenden. Geben Sie die gewünschte Anzahl an Komponenten und alle anderen Parameter an, die Sie verwenden möchten.

```python
# Fit a Gaussian Mixture Model
gmm = GaussianMixture(n_components=3)
gmm.fit(X_train)
```
