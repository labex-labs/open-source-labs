# 중심성 점수 계산

멱승 반복법을 사용하여 주요 고유 벡터 점수를 계산합니다.

```python
def centrality_scores(X, alpha=0.85, max_iter=100, tol=1e-10):
    """주요 고유 벡터의 멱승 반복 계산"""
    n = X.shape[0]
    X = X.copy()
    incoming_counts = np.asarray(X.sum(axis=1)).ravel()

    print("그래프 정규화")
    for i in incoming_counts.nonzero()[0]:
        X.data[X.indptr[i] : X.indptr[i + 1]] *= 1.0 / incoming_counts[i]
    dangle = np.asarray(np.where(np.isclose(X.sum(axis=1), 0), 1.0 / n, 0)).ravel()

    scores = np.full(n, 1.0 / n, dtype=np.float32)  # 초기 추정값
    for i in range(max_iter):
        print("멱승 반복 #%d" % i)
        prev_scores = scores
        scores = (
            alpha * (scores * X + np.dot(dangle, prev_scores))
            + (1 - alpha) * prev_scores.sum() / n
        )
        # 수렴 확인: 정규화된 l_inf 놈
        scores_max = np.abs(scores).max()
        if scores_max == 0.0:
            scores_max = 1.0
        err = np.abs(scores - prev_scores).max() / scores_max
        print("오차: %0.6f" % err)
        if err < n * tol:
            return scores

    return scores


print("멱승 반복법을 사용하여 주요 고유 벡터 점수를 계산합니다.")
scores = centrality_scores(X, max_iter=100)
```
