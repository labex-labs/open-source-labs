# NumPy のロゴを作成する

ここでは、`n_voxels`と呼ばれる 3 次元 NumPy 配列を使って NumPy のロゴを作成し始めます。配列内の特定の要素を`True`に設定して、ロゴの形状を表します。また、ボクセルに色を付けるために使われる`facecolors`と`edgecolors`と呼ばれる他の 2 つの NumPy 配列も定義します。

```python
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True

facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
```
