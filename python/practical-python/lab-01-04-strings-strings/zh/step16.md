# 练习 1.17：f 字符串

有时你想创建一个字符串，并将变量的值嵌入其中。

要做到这一点，请使用 f 字符串。例如：

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} shares of {name} at ${price:0.2f}'
'100 shares of IBM at $91.10'
>>>
```

修改练习 1.10 中的 `mortgage.py` 程序，使用 f 字符串来生成其输出。尽量使输出格式整齐。
