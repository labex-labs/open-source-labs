# 可能な解決策

k-meansクラスタリングの制限に対するいくつかの可能な解決策について議論します。次のコードブロックでは、最初のデータセットに対して正しいクラスタ数を見つける方法と、ランダム初期化の数を増やすことでサイズが不均一なブロブを処理する方法を示します。

```python
y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("Optimal Number of Clusters")
plt.show()

y_pred = KMeans(n_clusters=3, n_init=10, random_state=random_state).fit_predict(
    X_filtered
)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Unevenly Sized Blobs \nwith several initializations")
plt.show()
```
