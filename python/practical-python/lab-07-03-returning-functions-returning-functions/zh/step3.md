# 闭包

当一个内部函数作为结果被返回时，该内部函数被称为**闭包**。

```python
def add(x, y):
    # `do_add` 是一个闭包
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

**基本特性：闭包会保留函数稍后正常运行所需的所有变量的值**。可以将闭包看作是一个函数加上一个额外的环境，该环境保存了它所依赖的变量的值。
