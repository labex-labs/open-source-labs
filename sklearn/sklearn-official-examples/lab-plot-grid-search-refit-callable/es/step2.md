# Definir funciones

Definiremos dos funciones que se utilizarán más adelante en el laboratorio.

```python
def lower_bound(cv_results):
    """
    Calcular el límite inferior dentro de 1 desviación estándar
    de la mejor `mean_test_scores`.

    Parámetros
    ----------
    cv_results : dict de ndarrays de numpy(masked)
        Ver atributo cv_results_ de `GridSearchCV`

    Devuelve
    -------
    float
        Límite inferior dentro de 1 desviación estándar de la
        mejor `mean_test_score`.
    """
    best_score_idx = np.argmax(cv_results["mean_test_score"])

    return (
        cv_results["mean_test_score"][best_score_idx]
        - cv_results["std_test_score"][best_score_idx]
    )


def best_low_complexity(cv_results):
    """
    Equilibrar la complejidad del modelo con la puntuación validada cruzada.

    Parámetros
    ----------
    cv_results : dict de ndarrays de numpy(masked)
        Ver atributo cv_results_ de `GridSearchCV`.

    Devuelve
    ------
    int
        Índice de un modelo que tiene el menor número de componentes PCA
        mientras que su puntuación de prueba está dentro de 1 desviación estándar de la mejor
        `mean_test_score`.
    """
    threshold = lower_bound(cv_results)
    candidate_idx = np.flatnonzero(cv_results["mean_test_score"] >= threshold)
    best_idx = candidate_idx[
        cv_results["param_reduce_dim__n_components"][candidate_idx].argmin()
    ]
    return best_idx
```
