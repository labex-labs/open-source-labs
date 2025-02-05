# 创建半径和角度空间

我们将使用 `linspace` 函数创建半径和角度空间：

```python
# 生成半径和角度空间（省略 r=0 的半径以消除重复）。
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]
```
