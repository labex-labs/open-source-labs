# Lambda：匿名函数

使用 lambda 表达式来代替创建函数。在我们之前的排序示例中：

```python
portfolio.sort(key=lambda s: s['name'])
```

这创建了一个 **未命名** 的函数，该函数计算 **单个** 表达式。上述代码比初始代码短得多。

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# 与 lambda 对比
portfolio.sort(key=lambda s: s['name'])
```
