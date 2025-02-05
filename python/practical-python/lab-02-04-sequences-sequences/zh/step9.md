# enumerate() 函数

`enumerate` 函数会在迭代时额外添加一个计数器值。

```python
names = ['Elwood', 'Jake', 'Curtis']
for i, name in enumerate(names):
    # 循环时 i = 0，name = 'Elwood'
    # i = 1，name = 'Jake'
    # i = 2，name = 'Curtis'
```

一般形式为 `enumerate(sequence [, start = 0])`。`start` 是可选的。使用 `enumerate()` 的一个很好的例子是在读取文件时跟踪行号：

```python
with open(filename) as f:
    for lineno, line in enumerate(f, start=1):
     ...
```

最终，`enumerate` 只是以下代码的一个便捷写法：

```python
i = 0
for x in s:
    statements
    i += 1
```

使用 `enumerate` 可以减少输入量，并且运行速度稍快一些。
