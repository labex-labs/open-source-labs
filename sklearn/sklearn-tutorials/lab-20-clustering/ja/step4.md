# k-means クラスタリングを実行する

次に、k-means クラスタリングアルゴリズムをデータに適用しましょう。

```python
# Perform K-Means clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
```
