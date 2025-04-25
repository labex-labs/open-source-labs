# 创建一个文本图形对象

接下来，你将使用`matplotlib.text`中的`Text`类创建一个文本图形对象。你可以将 x 和 y 坐标、文本标签、水平和垂直对齐方式以及坐标轴对象作为参数进行指定。

```python
t = text.Text(3, 2.5, 'text label', ha='left', va='bottom', axes=ax)
```
