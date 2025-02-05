# 向绘图中添加文本

我们可以使用`text`函数向绘图中添加文本。我们可以指定文本的位置、旋转角度、水平和垂直对齐方式以及多行对齐方式。

```python
ax0.text(2, 7, 'this is\nyet another test',
         rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')
```
