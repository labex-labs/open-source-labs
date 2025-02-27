# Anpassen des elastischen Netzes

Wir können nun mit der Anpassung fortfahren. Wir müssen die zentrierte Designmatrix an `fit` übergeben, um zu verhindern, dass der elastische Netz-Schätzer erkennt, dass sie nicht zentriert ist und die von uns übergebene Gram-Matrix verwirft. Wenn wir jedoch die skalierte Designmatrix übergeben, wird der Vorverarbeitungscode sie falsch wieder skalieren. Wir übergeben auch die normalisierten Gewichte an den `sample_weight`-Parameter der `fit`-Funktion.

```python
from sklearn.linear_model import ElasticNet

lm = ElasticNet(alpha=0.01, precompute=gram)
lm.fit(X_centered, y, sample_weight=normalized_weights)
```
