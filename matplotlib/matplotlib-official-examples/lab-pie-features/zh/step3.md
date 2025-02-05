# 创建饼图

要创建饼图，我们将使用 Matplotlib 中的 `pie()` 函数。

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
```
