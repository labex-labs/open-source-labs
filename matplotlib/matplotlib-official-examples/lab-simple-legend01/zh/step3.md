# 给绘图添加图例

现在我们要给绘图添加一个图例。在 Matplotlib 中有两种添加图例的方法。在这个例子中我们将两种方法都使用。

```python
# 方法 1：将图例放置在子图上方
ax.legend(bbox_to_anchor=(0., 1.02, 1.,.102), loc='lower left',
           ncols=2, mode="expand", borderaxespad=0.)

# 方法 2：将图例放置在子图右侧
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
```
