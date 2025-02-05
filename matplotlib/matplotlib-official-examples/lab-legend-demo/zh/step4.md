# 使用多个图例键创建图例条目

在这一步中，我们将使用多个图例键来创建图例条目。

```python
# 定义图表数据
fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
p1 = ax1.scatter([1], [5], c='r', marker='s', s=100)
p2 = ax1.scatter([3], [2], c='b', marker='o', s=100)
p3, = ax1.plot([1, 5], [4, 4],'m-d')

# 为一个条目创建一个包含两个键的图例
l = ax1.legend([(p1, p3), p2], ['两个键', '一个键'], scatterpoints=1,
               numpoints=1, handler_map={tuple: HandlerTuple(ndivide=None)})

# 相互堆叠创建两个柱状图，并更改图例键之间的填充
x_left = [1, 2, 3]
y_pos = [1, 3, 2]
y_neg = [2, 1, 4]
rneg = ax2.bar(x_left, y_neg, width=0.5, color='w', hatch='///', label='-1')
rpos = ax2.bar(x_left, y_pos, width=0.5, color='k', label='+1')

# 通过使用特定的 `HandlerTuple` 对每个图例条目进行不同的处理
l = ax2.legend([(rpos, rneg), (rneg, rpos)], ['填充!=0', '填充=0'],
               handler_map={(rpos, rneg): HandlerTuple(ndivide=None),
                            (rneg, rpos): HandlerTuple(ndivide=None, pad=0.)})

# 显示图表
plt.show()
```
