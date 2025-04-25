# 给 X 轴和 Y 轴都添加限制

最后，我们将给 X 轴和 Y 轴都添加限制。我们将使用`xlolims`和`xuplims`参数给 X 轴误差线添加限制。

```python
# 绘制一个在 X 和 Y 方向都有下限和上限的序列
# X 误差恒定，Y 误差变化
xerr = 0.2
yerr = np.full_like(x, 0.2)
yerr[[3, 6]] = 0.3

# 通过修改之前的数据模拟一些限制
xlolims = lolims
xuplims = uplims
lolims = np.zeros_like(x)
uplims = np.zeros_like(x)
lolims[[6]] = True  # 仅在此索引处有限制
uplims[[3]] = True  # 仅在此索引处有限制

# 进行绘图
ax.errorbar(x, y + 2.1, xerr=xerr, yerr=yerr,
            xlolims=xlolims, xuplims=xuplims,
            uplims=uplims, lolims=lolims,
            marker='o', markersize=8, linestyle='none')
```
