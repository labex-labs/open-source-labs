# 计算电场

```python
tci = CubicTriInterpolator(triang, -V)

(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
```

解释：

- `CubicTriInterpolator` 是一个使用三次多项式进行数据插值的类。
- `tci` 是 `CubicTriInterpolator` 类的一个实例。
- `(Ex, Ey)` 是电场。
- `E_norm` 是归一化电场。
