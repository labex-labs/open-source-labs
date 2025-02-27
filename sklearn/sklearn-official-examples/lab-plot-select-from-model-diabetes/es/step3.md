# Selección de características basadas en importancia

Seleccionamos las dos características que son las más importantes de acuerdo con los coeficientes utilizando `SelectFromModel`. `SelectFromModel` acepta un parámetro `threshold` y seleccionará las características cuya importancia (definida por los coeficientes) sea superior a este umbral.

```python
from sklearn.feature_selection import SelectFromModel

threshold = np.sort(importance)[-3] + 0.01

sfm = SelectFromModel(ridge, threshold=threshold).fit(X, y)
print(f"Features selected by SelectFromModel: {feature_names[sfm.get_support()]}")
```
