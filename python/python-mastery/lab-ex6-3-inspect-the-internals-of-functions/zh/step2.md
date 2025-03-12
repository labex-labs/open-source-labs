# 使用 `inspect` 模块

在 Python 中，标准库提供了一个非常有用的 `inspect` 模块。这个模块就像一个侦探工具，能帮助我们收集 Python 中活动对象（live objects）的信息。活动对象可以是模块、类和函数等。与手动挖掘对象的属性来查找信息不同，`inspect` 模块提供了更有条理、更高级的方式来了解函数的属性。

让我们继续使用同一个 Python 交互式 shell 来探索这个模块的工作原理。

## 函数签名

`inspect.signature()` 函数是一个实用工具。当你将一个函数传递给它时，它会返回一个 `Signature` 对象。这个对象包含了函数参数的重要细节。

以下是一个示例。假设我们有一个名为 `add` 的函数。我们可以使用 `inspect.signature()` 函数来获取它的签名：

```python
import inspect
sig = inspect.signature(add)
print(sig)
```

当你运行这段代码时，输出将是：

```
(x, y)
```

这个输出展示了函数的签名，它告诉我们函数可以接受哪些参数。

## 检查参数细节

我们可以更进一步，获取函数每个参数的更深入信息。

```python
print(sig.parameters)
```

这段代码的输出将是：

```
OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)])
```

函数的参数存储在一个有序字典中。有时，我们可能只对参数的名称感兴趣。我们可以将这个有序字典转换为元组，以提取参数名称。

```python
param_names = tuple(sig.parameters)
print(param_names)
```

输出将是：

```
('x', 'y')
```

## 检查单个参数

我们还可以仔细查看每个单独的参数。以下代码会遍历函数中的每个参数，并打印出关于它的一些重要细节。

```python
for name, param in sig.parameters.items():
    print(f"Parameter: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default if param.default is not param.empty else 'No default'}")
```

这段代码将向我们展示每个参数的详细信息。它会告诉我们参数的类型（是位置参数、关键字参数等）以及是否有默认值。

`inspect` 模块还有许多其他用于函数自省（introspection）的实用函数。以下是一些示例：

- `inspect.getdoc(obj)`：这个函数用于获取对象的文档字符串。文档字符串就像是程序员为解释对象的功能而编写的注释。
- `inspect.getfile(obj)`：它帮助我们找出对象定义所在的文件。当我们想要定位对象的源代码时，这非常有用。
- `inspect.getsource(obj)`：这个函数用于获取对象的源代码。它让我们能够确切地看到对象是如何实现的。
