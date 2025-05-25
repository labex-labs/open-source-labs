# Definir Funções

Vamos definir duas funções que serão usadas mais tarde no laboratório.

```python
def lower_bound(cv_results):
    """
    Calcula o limite inferior dentro de 1 desvio padrão
    das melhores `mean_test_scores`.

    Parâmetros
    ----------
    cv_results : dict de numpy(masked) ndarrays
        Veja o atributo cv_results_ de `GridSearchCV`

    Retorna
    -------
    float
        Limite inferior dentro de 1 desvio padrão da
        melhor `mean_test_score`.
    """
    best_score_idx = np.argmax(cv_results["mean_test_score"])

    return (
        cv_results["mean_test_score"][best_score_idx]
        - cv_results["std_test_score"][best_score_idx]
    )


def best_low_complexity(cv_results):
    """
    Equilibra a complexidade do modelo com a pontuação cruzada.

    Parâmetros
    ----------
    cv_results : dict de numpy(masked) ndarrays
        Veja o atributo cv_results_ de `GridSearchCV`.

    Retorno
    ------
    int
        Índice de um modelo que tem o menor número de componentes PCA
        enquanto tem sua pontuação de teste dentro de 1 desvio padrão da melhor
        `mean_test_score`.
    """
    threshold = lower_bound(cv_results)
    candidate_idx = np.flatnonzero(cv_results["mean_test_score"] >= threshold)
    best_idx = candidate_idx[
        cv_results["param_reduce_dim__n_components"][candidate_idx].argmin()
    ]
    return best_idx
```
