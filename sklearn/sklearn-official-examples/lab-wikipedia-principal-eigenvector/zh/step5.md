# 计算中心性得分

我们将使用幂迭代法来计算主特征向量得分。

```python
def centrality_scores(X, alpha=0.85, max_iter=100, tol=1e-10):
    """Power iteration computation of the principal eigenvector"""
    n = X.shape[0]
    X = X.copy()
    incoming_counts = np.asarray(X.sum(axis=1)).ravel()

    print("Normalizing the graph")
    for i in incoming_counts.nonzero()[0]:
        X.data[X.indptr[i] : X.indptr[i + 1]] *= 1.0 / incoming_counts[i]
    dangle = np.asarray(np.where(np.isclose(X.sum(axis=1), 0), 1.0 / n, 0)).ravel()

    scores = np.full(n, 1.0 / n, dtype=np.float32)  # initial guess
    for i in range(max_iter):
        print("power iteration #%d" % i)
        prev_scores = scores
        scores = (
            alpha * (scores * X + np.dot(dangle, prev_scores))
            + (1 - alpha) * prev_scores.sum() / n
        )
        # check convergence: normalized l_inf norm
        scores_max = np.abs(scores).max()
        if scores_max == 0.0:
            scores_max = 1.0
        err = np.abs(scores - prev_scores).max() / scores_max
        print("error: %0.6f" % err)
        if err < n * tol:
            return scores

    return scores


print("Computing principal eigenvector score using a power iteration method")
scores = centrality_scores(X, max_iter=100)
```
