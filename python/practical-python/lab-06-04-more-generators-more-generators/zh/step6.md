# 练习 6.15：代码简化

生成器表达式常常是小型生成器函数的有用替代品。例如，不用编写这样的函数：

```python
def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

你可以编写如下代码：

```python
rows = (row for row in rows if row['name'] in names)
```

修改 `ticker.py` 程序，酌情使用生成器表达式。
