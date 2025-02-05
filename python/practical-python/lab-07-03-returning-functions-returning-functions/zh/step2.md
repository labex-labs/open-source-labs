# 局部变量

观察内部函数如何引用外部函数定义的变量。

```python
def add(x, y):
    def do_add():
        # `x` 和 `y` 在 `add(x, y)` 之上定义
        print('Adding', x, y)
        return x + y
    return do_add
```

进一步观察，在 `add()` 完成后，这些变量不知为何仍然存在。

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4      # 这些值从哪里来？
7
```
