# Definir os Classificadores de Conjunto

Definiremos uma lista de três classificadores Random Forest, cada um com um valor diferente para o parâmetro `max_features`. Definiremos o parâmetro de construção `warm_start` como `True` para permitir o acompanhamento da taxa de erro OOB durante o treinamento. Também definiremos o parâmetro `oob_score` como `True` para permitir o cálculo da taxa de erro OOB.

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
