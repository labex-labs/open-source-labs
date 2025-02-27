# Selección de características univariadas

A continuación, realizaremos la selección de características univariadas con una prueba F para la puntuación de características. Utilizaremos la función de selección predeterminada para seleccionar las cuatro características más significativas.

```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=4)
selector.fit(X_train, y_train)
scores = -np.log10(selector.pvalues_)
scores /= scores.max()
```
