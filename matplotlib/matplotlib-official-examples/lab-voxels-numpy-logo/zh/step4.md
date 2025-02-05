# 放大体素图像

我们现在使用之前定义的 `explode` 函数来放大体素图像，使每个体素之间留出间隙。

```python
filled = np.ones(n_voxels.shape)
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)
```
