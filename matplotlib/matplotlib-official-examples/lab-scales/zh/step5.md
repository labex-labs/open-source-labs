# 创建对数几率比例图

我们要探索的第四种比例变换类型是对数几率（logit）比例。当处理取值范围在 0 到 1 之间的数据时，这种比例类型很有用。要创建对数几率比例图，我们使用 `set_yscale()` 方法并传入字符串 `'logit'`。我们还会给图添加标题和网格。

```python
# logit
plt.plot(x, y)
plt.yscale('logit')
plt.title('Logit Scale')
plt.grid(True)
```
