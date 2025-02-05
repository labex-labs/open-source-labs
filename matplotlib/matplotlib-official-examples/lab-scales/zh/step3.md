# 创建对数比例图

我们接下来要探索的比例变换类型是对数比例。要创建对数比例图，我们使用 `set_yscale()` 方法并传入字符串 `'log'`。我们同样会给图添加标题和网格。

```python
# log
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic Scale')
plt.grid(True)
```
