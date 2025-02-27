# K-Means クラスタリングの適用

次に、K-Means クラスタリングアルゴリズムをデータに適用します。アルゴリズムを 3 つのクラスタで初期化し、データに適合させます。

```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
```
