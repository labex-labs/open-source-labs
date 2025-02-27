# Definir parámetros

Definiremos los parámetros para nuestro clasificador Gradient Boosting. Utilizaremos los siguientes parámetros:

- n_estimators: número de etapas de potenciación a realizar
- max_leaf_nodes: número máximo de nodos hoja en cada árbol
- max_depth: profundidad máxima del árbol
- random_state: semilla aleatoria para la consistencia
- min_samples_split: número mínimo de muestras necesarias para dividir un nodo interno

```python
original_params = {
    "n_estimators": 400,
    "max_leaf_nodes": 4,
    "max_depth": None,
    "random_state": 2,
    "min_samples_split": 5,
}
```
