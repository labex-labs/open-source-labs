# Die Daten gruppieren

Sobald das Modell angepasst ist, können wir es verwenden, um die Daten zu gruppieren, indem wir jeder Probe die zugehörige Gauß-Komponente zuweisen. Die `predict`-Methode der `GaussianMixture`-Klasse kann dazu verwendet werden.

```python
# Cluster the data
cluster_labels = gmm.predict(X_test)
```
