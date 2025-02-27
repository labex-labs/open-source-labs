# Selección de características con selección secuencial de características

Utilizamos el Selector Secuencial de Características (SFS) para seleccionar características. El SFS es un procedimiento voraz donde, en cada iteración, elegimos la mejor nueva característica para agregar a nuestras características seleccionadas basadas en una puntuación de validación cruzada. También podemos ir en la dirección inversa (SFS hacia atrás), es decir, comenzar con todas las características y elegir vorazmente características para eliminar una por una.

```python
from sklearn.feature_selection import SequentialFeatureSelector

sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="forward").fit(X, y)
sfs_backward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="backward").fit(X, y)

print(f"Features selected by forward sequential selection: {feature_names[sfs_forward.get_support()]}")
print(f"Features selected by backward sequential selection: {feature_names[sfs_backward.get_support()]}")
```
