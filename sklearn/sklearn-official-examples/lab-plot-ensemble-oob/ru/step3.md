# Определяем ансамбли классификаторов

Мы определим список из трех классификаторов Случайный лес, каждый с разным значением параметра `max_features`. Мы установим параметр конструкции `warm_start` в значение `True`, чтобы отслеживать ошибку вне пакета (Out-Of-Bag, OOB) во время обучения. Также установим параметр `oob_score` в значение `True`, чтобы включить вычисление ошибки вне пакета.

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
