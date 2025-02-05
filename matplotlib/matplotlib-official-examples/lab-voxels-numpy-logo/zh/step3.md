# 构建 NumPy 标志

现在我们可以开始使用一个名为 `n_voxels` 的 3D NumPy 数组来构建 NumPy 标志了。我们将数组中的某些元素设置为 `True` 以表示标志的形状。我们还定义了另外两个 NumPy 数组，名为 `facecolors` 和 `edgecolors`，它们将用于为体素着色。

```python
n_voxels = np.zeros((4, 3, 4), dtype=bool)
n_voxels[0, 0, :] = True
n_voxels[-1, 0, :] = True
n_voxels[1, 0, 2] = True
n_voxels[2, 0, 1] = True

facecolors = np.where(n_voxels, '#FFD65DC0', '#7A88CCC0')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
```
