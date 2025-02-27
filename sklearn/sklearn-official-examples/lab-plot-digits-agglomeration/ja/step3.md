# 接続行列の定義

このステップでは、scikit-learnの`grid_to_graph`関数を使って接続行列を定義します。この関数は、画像のピクセルグリッドに基づいて接続グラフを作成します。

```python
connectivity = grid_to_graph(*images[0].shape)
```
