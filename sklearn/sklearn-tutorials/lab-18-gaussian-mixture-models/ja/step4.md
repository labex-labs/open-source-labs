# データをクラスタリングする

モデルがフィットされたら、それを使って各サンプルを所属するガウスコンポーネントに割り当てることでデータをクラスタリングできます。この目的には、`GaussianMixture` クラスの `predict` メソッドを使用できます。

```python
# Cluster the data
cluster_labels = gmm.predict(X_test)
```
