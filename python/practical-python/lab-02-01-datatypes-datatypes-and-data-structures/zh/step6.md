# 元组解包

要在其他地方使用元组，你可以将其各个部分解包到变量中。

```python
name, shares, price = s
print('Cost', shares * price)
```

左边变量的数量必须与元组结构匹配。

```python
name, shares = s     # 错误
Traceback (most recent call last):
...
ValueError: too many values to unpack
```
