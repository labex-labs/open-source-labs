# スペクトラルバイクラスタリングを実行する

次に、スペクトラルバイクラスタリングアルゴリズムを使用してバイクラスタリングを実行しましょう。このアルゴリズムは、データ行列が隠されたチェッカーボード構造を持っていることを前提としています。

```python
# Initialize and fit the Spectral Biclustering model
model_bi = SpectralBiclustering(n_clusters=(2, 3), random_state=0)
model_bi.fit(data)

# Get row and column cluster membership
row_clusters_bi = model_bi.row_labels_
column_clusters_bi = model_bi.column_labels_
```
