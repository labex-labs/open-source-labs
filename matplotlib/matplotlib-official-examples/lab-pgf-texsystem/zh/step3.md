# 创建图表

现在，你可以使用 `plt.subplots()` 函数来创建图表。在本示例中，我们将创建一个简单的折线图。

```python
fig, ax = plt.subplots(figsize=(4.5, 2.5))

ax.plot(range(5))
```
