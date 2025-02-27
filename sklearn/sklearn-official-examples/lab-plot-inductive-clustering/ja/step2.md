# クラスタリングアルゴリズムの学習

このステップでは、生成した学習データに対してクラスタリングアルゴリズムを学習し、クラスタラベルを取得します。scikit - learnの`AgglomerativeClustering`を使って、3つのクラスタでアルゴリズムを学習します。

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```
