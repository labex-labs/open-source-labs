# 使用 `from module import` 语法

在 Python 中，有多种从模块导入组件的方式。其中一种方式是 `from module import` 语法，我们将在本节中探讨这种语法。

当你从模块导入组件时，通常最好从一个全新的状态开始。这能确保没有之前操作遗留的变量或设置干扰我们当前的实验。

1. 重启 Python 解释器以获得全新状态：

```python
>>> exit()
```

此命令会退出当前的 Python 解释器会话。退出后，我们将启动一个新会话以确保环境是全新的。

```bash
python3
```

这个 bash 命令会启动一个新的 Python 3 解释器会话。现在我们有了一个全新的 Python 环境，可以开始从模块导入组件了。

2. 使用 `from module import` 语法从模块导入特定组件：

```python
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
```

在这里，我们使用 `from simplemod import foo` 语句仅从 `simplemod` 模块导入 `foo` 函数。注意，尽管我们只请求了 `foo` 函数，但整个 `simplemod` 模块都被加载了。这可以从“Loaded simplemod”输出看出来。原因是 Python 需要加载整个模块才能访问 `foo` 函数。

3. 使用 `from module import` 时，你无法直接访问模块本身：

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
```

当我们使用 `from module import` 语法时，我们只是将指定的组件直接引入到我们的命名空间中。模块名本身并没有被导入。所以，当我们尝试访问 `simplemod.foo()` 时，Python 不识别 `simplemod`，因为它不是以这种方式导入的。

4. 你可以一次导入多个组件：

```python
>>> from simplemod import x, foo
>>> x
42
>>> foo()
x is 42
```

`from module import` 语法允许我们在一条语句中从模块导入多个组件。这里，我们从 `simplemod` 模块同时导入了变量 `x` 和函数 `foo`。导入后，我们可以在代码中直接访问这些组件。

5. 当你从模块导入一个变量时，你是在创建一个对该对象的新引用，而不是与模块中的变量建立链接：

```python
>>> x = 13  # Change the local variable x
>>> x
13
>>> foo()
x is 42  # The function still uses the module's x, not your local x
```

当我们从模块导入一个变量时，实际上是在我们的局部命名空间中创建了一个对同一对象的新引用。所以，当我们将局部变量 `x` 更改为 `13` 时，它不会影响 `simplemod` 模块内的 `x` 变量。`foo()` 函数仍然引用模块中的 `x` 变量，其值为 `42`。理解这个概念对于避免代码中的混淆至关重要。
