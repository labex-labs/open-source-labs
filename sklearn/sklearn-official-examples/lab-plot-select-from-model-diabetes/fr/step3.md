# Sélection de fonctionnalités basée sur l'importance

Nous sélectionnons les deux fonctionnalités qui sont les plus importantes selon les coefficients en utilisant `SelectFromModel`. `SelectFromModel` accepte un paramètre `seuil` et sélectionnera les fonctionnalités dont l'importance (définie par les coefficients) est supérieure à ce seuil.

```python
from sklearn.feature_selection import SelectFromModel

threshold = np.sort(importance)[-3] + 0.01

sfm = SelectFromModel(ridge, threshold=threshold).fit(X, y)
print(f"Features selected by SelectFromModel: {feature_names[sfm.get_support()]}")
```
