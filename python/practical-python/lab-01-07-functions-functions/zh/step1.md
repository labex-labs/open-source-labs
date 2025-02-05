# 自定义函数

对于你想要复用的代码，可以使用函数。以下是一个函数定义：

```python
def sumcount(n):
    '''
    返回前 n 个整数的和
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total
```

要调用一个函数：

```python
a = sumcount(100)
```

函数是执行某些任务并返回结果的一系列语句。需要使用 `return` 关键字来明确指定函数的返回值。
