# 多个返回值

函数只能返回一个值。不过，函数可以通过返回一个元组来返回多个值。

```python
def divide(a,b):
    q = a // b      # 商
    r = a % b       # 余数
    return q, r     # 返回一个元组
```

用法示例：

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```
