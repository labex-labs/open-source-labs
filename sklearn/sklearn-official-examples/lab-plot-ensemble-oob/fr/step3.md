# Définir les classifieurs d'ensemble

Nous allons définir une liste de trois classifieurs Random Forest, chacun avec une valeur différente pour le paramètre `max_features`. Nous allons définir le paramètre de construction `warm_start` sur `True` pour activer le suivi du taux d'erreur hors-bag (OOB) pendant l'entraînement. Nous allons également définir le paramètre `oob_score` sur `True` pour activer le calcul du taux d'erreur hors-bag.

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
