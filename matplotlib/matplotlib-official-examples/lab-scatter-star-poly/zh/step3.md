# 创建子图

我们将使用 `subplots()` 函数创建一个 2x3 的子图网格。

```python
fig, axs = plt.subplots(2, 3, sharex=True, sharey=True, layout="constrained")
```
