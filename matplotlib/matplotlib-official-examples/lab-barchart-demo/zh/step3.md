# 定义辅助函数

我们定义两个辅助函数。第一个函数 `to_ordinal`，将整数转换为序数词字符串（例如，2 -> '2nd'）。第二个函数 `format_score`，为右 y 轴创建分数标签，格式为测试名称后跟测量单位（如果有），分两行显示。

```python
def to_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    return v + suffixes[v[-1]]

def format_score(score):
    return f'{score.value}\n{score.unit}' if score.unit else str(score.value)
```
