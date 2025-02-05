# 创建线性比例图

我们要探索的第一种比例变换类型是线性比例。这是 Matplotlib 中使用的默认比例。要创建线性比例图，我们使用 `set_yscale()` 方法并传入字符串 `'linear'`。我们还会给图添加标题和网格。

```python
# linear
plt.plot(x, y)
plt.yscale('linear')
plt.title('Linear Scale')
plt.grid(True)
```
