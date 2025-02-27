# Calcul des scores de centralité

Nous allons calculer le score du vecteur propre principal à l'aide d'une méthode d'itération de puissance.

```python
def centrality_scores(X, alpha=0.85, max_iter=100, tol=1e-10):
    """Calcul d'itération de puissance du vecteur propre principal"""
    n = X.shape[0]
    X = X.copy()
    incoming_counts = np.asarray(X.sum(axis=1)).ravel()

    print("Normalisation du graphe")
    for i in incoming_counts.nonzero()[0]:
        X.data[X.indptr[i] : X.indptr[i + 1]] *= 1.0 / incoming_counts[i]
    dangle = np.asarray(np.where(np.isclose(X.sum(axis=1), 0), 1.0 / n, 0)).ravel()

    scores = np.full(n, 1.0 / n, dtype=np.float32)  # estimation initiale
    for i in range(max_iter):
        print("itération de puissance #%d" % i)
        prev_scores = scores
        scores = (
            alpha * (scores * X + np.dot(dangle, prev_scores))
            + (1 - alpha) * prev_scores.sum() / n
        )
        # vérification de la convergence : norme l_inf normalisée
        scores_max = np.abs(scores).max()
        if scores_max == 0.0:
            scores_max = 1.0
        err = np.abs(scores - prev_scores).max() / scores_max
        print("erreur : %0.6f" % err)
        if err < n * tol:
            return scores

    return scores


print("Calcul du score du vecteur propre principal à l'aide d'une méthode d'itération de puissance")
scores = centrality_scores(X, max_iter=100)
```
