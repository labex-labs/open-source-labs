# 自定义轴标签

要自定义轴标签，我们可以使用`set_xlabel`和`set_ylabel`函数。我们还可以使用“\n”字符添加换行符。

```python
ax0.set_xlabel('this is a xlabel\n(with newlines!)')
ax0.set_ylabel('this is vertical\ntest', multialignment='center')
```
