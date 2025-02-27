# Definir los clasificadores de conjunto

Definiremos una lista de tres clasificadores de bosque aleatorio, cada uno con un valor diferente para el parámetro `max_features`. Estableceremos el parámetro de construcción `warm_start` en `True` para habilitar el seguimiento de la tasa de error OOB durante el entrenamiento. También estableceremos el parámetro `oob_score` en `True` para habilitar el cálculo de la tasa de error OOB.

```python
ensemble_clfs = [
    (
        "RandomForestClassifier, max_features='sqrt'",
        RandomForestClassifier(
            warm_start=True,
            oob_score=True,
            max_features="sqrt",
            random_state=RANDOM_STATE,
        ),
    ),
    (
        "RandomForestClassifier, max_features='log2'",
        RandomForestClassifier(
            warm_start=True,
            max_features="log2",
            oob_score=True,
            random_state=RANDOM_STATE,
        ),
    ),
    (
        "RandomForestClassifier, max_features=None",
        RandomForestClassifier(
            warm_start=True,
            max_features=None,
            oob_score=True,
            random_state=RANDOM_STATE,
        ),
    ),
]
```
