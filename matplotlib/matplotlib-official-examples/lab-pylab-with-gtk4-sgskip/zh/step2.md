# 创建图形和子图

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```

我们创建一个包含两个子图的图形，并在上面绘制两组数据。我们还为这些子图添加了一个图例。
