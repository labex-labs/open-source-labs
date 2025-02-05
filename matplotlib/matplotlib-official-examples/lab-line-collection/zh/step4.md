# 创建绘图

现在我们可以使用`matplotlib`创建一个绘图，并使用`Axes`对象的`add_collection`方法将`LineCollection`对象添加到绘图中。

```python
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(ys.min(), ys.max())

ax.add_collection(line_segments)
ax.set_title('Line collection with masked arrays')
plt.show()
```
