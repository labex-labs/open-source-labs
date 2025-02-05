# 创建一个带标签的简单等高线图

现在我们已经有了数据，就可以使用默认颜色创建一个带标签的简单等高线图。

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
```
