# Funktionen definieren

Wir werden zwei Funktionen definieren, die später im Lab verwendet werden.

```python
def lower_bound(cv_results):
    """
    Berechnet die untere Grenze innerhalb von 1 Standardabweichung
    der besten `mean_test_scores`.

    Parameter
    ----------
    cv_results : dict von numpy(masked) ndarrays
        Siehe Attribut cv_results_ von `GridSearchCV`

    Rückgabe
    -------
    float
        Untere Grenze innerhalb von 1 Standardabweichung der
        besten `mean_test_score`.
    """
    best_score_idx = np.argmax(cv_results["mean_test_score"])

    return (
        cv_results["mean_test_score"][best_score_idx]
        - cv_results["std_test_score"][best_score_idx]
    )


def best_low_complexity(cv_results):
    """
    Stellt ein Gleichgewicht zwischen Modellkomplexität und
    durch Kreuzvalidierung ermittelter Punktzahl her.

    Parameter
    ----------
    cv_results : dict von numpy(masked) ndarrays
        Siehe Attribut cv_results_ von `GridSearchCV`.

    Rückgabe
    ------
    int
        Index eines Modells, das die wenigsten PCA-Komponenten hat,
        während dessen Testscore innerhalb von 1 Standardabweichung der besten
        `mean_test_score` liegt.
    """
    threshold = lower_bound(cv_results)
    candidate_idx = np.flatnonzero(cv_results["mean_test_score"] >= threshold)
    best_idx = candidate_idx[
        cv_results["param_reduce_dim__n_components"][candidate_idx].argmin()
    ]
    return best_idx
```
