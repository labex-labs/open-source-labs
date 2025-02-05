# 验证（再探讨）

在上一个练习中，你编写了一个 `@validated` 装饰器来强制使用类型注释。例如：

```python
@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y
```

创建一个新的装饰器 `@enforce()`，它改为通过装饰器的关键字参数来强制指定类型。例如：

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

被装饰函数的最终行为应该是相同的。注意：使用 `return_` 关键字来指定返回类型。`return` 是 Python 的保留字，所以你必须选择一个稍有不同的名称。

**讨论**

编写健壮的装饰器通常比看起来要困难得多。推荐阅读：
