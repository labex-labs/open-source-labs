# 自定义 X 轴标签

要自定义 X 轴标签，我们可以使用`set_xticks`函数。我们可以指定刻度的位置和标签。

```python
ax1.set_xticks([0.2, 0.4, 0.6, 0.8, 1.],
               labels=["Jan\n2009", "Feb\n2009", "Mar\n2009", "Apr\n2009",
                       "May\n2009"])
```
