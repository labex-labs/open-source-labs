# Definieren der Ensemble-Klassifizierer

Wir werden eine Liste von drei Random Forest-Klassifizierern definieren, wobei jeder einen anderen Wert für den Parameter `max_features` hat. Wir setzen den Konstruktionsparameter `warm_start` auf `True`, um die Verfolgung der OOB-Fehlerrate während des Trainings zu ermöglichen. Wir setzen auch den Parameter `oob_score` auf `True`, um die Berechnung der OOB-Fehlerrate zu ermöglichen.

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
