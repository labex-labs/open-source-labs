# Define the Ensemble Classifiers

We will define a list of three Random Forest classifiers, each with a different value for the `max_features` parameter. We will set the `warm_start` construction parameter to `True` to enable tracking of the OOB error rate during training. We will also set the `oob_score` parameter to `True` to enable OOB error rate calculation.

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


