# Cálculo de puntuaciones de centralidad

Calcularemos la puntuación del eigenvector principal utilizando un método de iteración de potencia.

```python
def centrality_scores(X, alpha=0.85, max_iter=100, tol=1e-10):
    """Cálculo de iteración de potencia del eigenvector principal"""
    n = X.shape[0]
    X = X.copy()
    incoming_counts = np.asarray(X.sum(axis=1)).ravel()

    print("Normalizando el grafo")
    for i in incoming_counts.nonzero()[0]:
        X.data[X.indptr[i] : X.indptr[i + 1]] *= 1.0 / incoming_counts[i]
    dangle = np.asarray(np.where(np.isclose(X.sum(axis=1), 0), 1.0 / n, 0)).ravel()

    scores = np.full(n, 1.0 / n, dtype=np.float32)  # suposición inicial
    for i in range(max_iter):
        print("iteración de potencia #%d" % i)
        prev_scores = scores
        scores = (
            alpha * (scores * X + np.dot(dangle, prev_scores))
            + (1 - alpha) * prev_scores.sum() / n
        )
        # comprobar la convergencia: norma l_inf normalizada
        scores_max = np.abs(scores).max()
        if scores_max == 0.0:
            scores_max = 1.0
        err = np.abs(scores - prev_scores).max() / scores_max
        print("error: %0.6f" % err)
        if err < n * tol:
            return scores

    return scores


print("Calculando la puntuación del eigenvector principal utilizando un método de iteración de potencia")
scores = centrality_scores(X, max_iter=100)
```
