# クラスタリングアルゴリズムの学習

このステップでは、生成した学習データに対してクラスタリングアルゴリズムを学習し、クラスタラベルを取得します。scikit - learn の`AgglomerativeClustering`を使って、3 つのクラスタでアルゴリズムを学習します。

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```
