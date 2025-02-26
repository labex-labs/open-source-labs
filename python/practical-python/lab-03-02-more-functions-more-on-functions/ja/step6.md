# 複数の返却値

関数は1つの値のみを返すことができます。ただし、関数はタプルで値を返すことで複数の値を返すことができます。

```python
def divide(a,b):
    q = a // b      # 商
    r = a % b       # 余り
    return q, r     # タプルを返す
```

使用例:

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```
