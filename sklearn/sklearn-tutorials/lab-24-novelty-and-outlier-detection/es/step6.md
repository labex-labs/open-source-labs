# Acceder a las puntuaciones de valores atípicos

Además de predecir valores atípicos, también podemos acceder a las puntuaciones de valores atípicos para cada observación utilizando el atributo `negative_outlier_factor_`. Las puntuaciones de valores atípicos más bajas indican una mayor anomalía.

```python
outlier_scores = estimator.negative_outlier_factor_
print(outlier_scores)
```
