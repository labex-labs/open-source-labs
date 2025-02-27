# Définition de fonctions

Nous allons définir deux fonctions qui seront utilisées plus tard dans le laboratoire.

```python
def lower_bound(cv_results):
    """
    Calculer la borne inférieure à l'intérieur d'un écart-type
    du meilleur `mean_test_scores`.

    Paramètres
    ----------
    cv_results : dict de ndarrays numpy(masked)
        Voir l'attribut cv_results_ de `GridSearchCV`

    Retours
    -------
    float
        Borne inférieure à l'intérieur d'un écart-type du
        meilleur `mean_test_score`.
    """
    best_score_idx = np.argmax(cv_results["mean_test_score"])

    return (
        cv_results["mean_test_score"][best_score_idx]
        - cv_results["std_test_score"][best_score_idx]
    )


def best_low_complexity(cv_results):
    """
    Équilibrer la complexité du modèle avec le score de validation croisée.

    Paramètres
    ----------
    cv_results : dict de ndarrays numpy(masked)
        Voir l'attribut cv_results_ de `GridSearchCV`.

    Retour
    ------
    int
        Index d'un modèle qui a le nombre minimum de composants PCA
        tout en ayant son score de test à l'intérieur d'un écart-type du meilleur
        `mean_test_score`.
    """
    threshold = lower_bound(cv_results)
    candidate_idx = np.flatnonzero(cv_results["mean_test_score"] >= threshold)
    best_idx = candidate_idx[
        cv_results["param_reduce_dim__n_components"][candidate_idx].argmin()
    ]
    return best_idx
```
