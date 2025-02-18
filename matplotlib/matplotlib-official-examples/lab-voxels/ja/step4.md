# 色を設定する

ここで、ボクセルプロット内の各オブジェクトの色を設定します。これは、手順 3 で作成したブール配列と同じ形状の空の配列を作成し、各オブジェクトの位置に基づいて色を設定することで行います。

```python
colors = np.empty(voxelarray.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'
```
