# 全局定义

在**全局**作用域中定义的所有内容都会填充到模块命名空间中。假设有两个模块都定义了相同的变量 `x`。

```python
# foo.py
x = 42
def grok(a):
 ...
```

```python
# bar.py
x = 37
def spam(a):
 ...
```

在这种情况下，`x` 的定义引用了不同的变量。一个是 `foo.x`，另一个是 `bar.x`。不同的模块可以使用相同的名称，并且这些名称不会相互冲突。

**模块是相互隔离的**。
