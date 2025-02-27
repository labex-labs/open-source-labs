# k-meansクラスタリングを実行する

次に、k-meansクラスタリングアルゴリズムをデータに適用しましょう。

```python
# Perform K-Means clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
```
