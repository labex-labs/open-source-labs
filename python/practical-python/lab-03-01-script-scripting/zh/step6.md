# 函数定义

函数可以按任何顺序进行**定义**。

```python
def foo(x):
    bar(x)

def bar(x):
    statements

# 或者
def bar(x):
    statements

def foo(x):
    bar(x)
```

在程序执行期间，函数必须仅在实际被**使用**（或调用）之前进行定义。

```python
foo(3)        # foo 必须已经被定义
```

从风格上来说，函数以**自底向上**的方式进行定义可能更为常见。
