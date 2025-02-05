# 创建对称对数比例图

我们要探索的第三种比例变换类型是对称对数比例。当处理包含正值和负值的数据时，这种比例类型很有用。要创建对称对数比例图，我们使用 `set_yscale()` 方法并传入字符串 `'symlog'`。我们还将 `linthresh` 参数设置为 `0.02`，以指定零值附近将进行线性缩放的值范围。我们同样会给图添加标题和网格。

```python
# symmetric log
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.02)
plt.title('Symmetrical Logarithmic Scale')
plt.grid(True)
```
