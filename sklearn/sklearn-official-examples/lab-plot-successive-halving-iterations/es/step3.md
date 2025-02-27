# Definiendo el espacio de parámetros

Define un diccionario `param_dist` que contiene los hiperparámetros y sus respectivos valores para buscar. Los hiperparámetros son `max_depth`, `max_features`, `min_samples_split`, `bootstrap` y `criterion`. El rango de búsqueda para `max_features` y `min_samples_split` se define usando la función `randint` del módulo `scipy.stats`. El código para definir el espacio de parámetros es el siguiente:

```python
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 6),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}
```
