# 近傍点グラフの計算

このステップでは、KNeighborsTransformer を使って近傍点グラフを計算します。

```python
# この変換器は、グリッドサーチで必要な最大数の近傍点を使って近傍点グラフを計算します。
# 分類器モデルは、独自の n_neighbors パラメータに応じて近傍点グラフをフィルタリングします。
graph_model = KNeighborsTransformer(n_neighbors=max(n_neighbors_list), mode="distance")
```
