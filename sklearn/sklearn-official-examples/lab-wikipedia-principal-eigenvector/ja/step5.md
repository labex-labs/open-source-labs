# 中心性スコアの計算

パワー反復法を使って主固有ベクトルスコアを計算します。

```python
def centrality_scores(X, alpha=0.85, max_iter=100, tol=1e-10):
    """主固有ベクトルのパワー反復計算"""
    n = X.shape[0]
    X = X.copy()
    incoming_counts = np.asarray(X.sum(axis=1)).ravel()

    print("グラフを正規化中")
    for i in incoming_counts.nonzero()[0]:
        X.data[X.indptr[i] : X.indptr[i + 1]] *= 1.0 / incoming_counts[i]
    dangle = np.asarray(np.where(np.isclose(X.sum(axis=1), 0), 1.0 / n, 0)).ravel()

    scores = np.full(n, 1.0 / n, dtype=np.float32)  # 初期推定
    for i in range(max_iter):
        print("パワー反復 #%d" % i)
        prev_scores = scores
        scores = (
            alpha * (scores * X + np.dot(dangle, prev_scores))
            + (1 - alpha) * prev_scores.sum() / n
        )
        # 収束を確認する: 正規化されたl_infノルム
        scores_max = np.abs(scores).max()
        if scores_max == 0.0:
            scores_max = 1.0
        err = np.abs(scores - prev_scores).max() / scores_max
        print("エラー: %0.6f" % err)
        if err < n * tol:
            return scores

    return scores


print("パワー反復法を使って主固有ベクトルスコアを計算中")
scores = centrality_scores(X, max_iter=100)
```
