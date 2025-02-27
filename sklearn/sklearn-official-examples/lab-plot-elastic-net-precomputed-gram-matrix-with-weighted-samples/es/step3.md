# Ajustando la red elástica

Ahora podemos proceder con el ajuste. Debemos pasar la matriz de diseño centrada a `fit` para evitar que el estimador de la red elástica detecte que no está centrada y deseche la matriz de Gram que pasamos. Sin embargo, si pasamos la matriz de diseño escalada, el código de preprocesamiento la reescalará incorrectamente una segunda vez. También pasamos los pesos normalizados al parámetro `sample_weight` de la función `fit`.

```python
from sklearn.linear_model import ElasticNet

lm = ElasticNet(alpha=0.01, precompute=gram)
lm.fit(X_centered, y, sample_weight=normalized_weights)
```
