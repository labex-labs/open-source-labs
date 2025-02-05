# 创建一个格式化函数

我们创建一个格式化函数，该函数根据刻度处的值确定刻度标签。如果刻度值是`xs`范围内的整数，则返回`labels`列表中对应的标签。否则，返回一个空字符串。

```python
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''
```
