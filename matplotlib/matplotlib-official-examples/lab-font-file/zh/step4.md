# 设置标题的字体

我们使用`Axes`类的`set_title()`方法来设置图表标题的字体。我们将字体路径作为`font`参数传递，并将字体文件的名称作为图表的标题。

```python
ax.set_title(f'This is a special font: {fpath.name}', font=fpath)
```
