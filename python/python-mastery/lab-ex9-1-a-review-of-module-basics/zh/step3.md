# 理解模块加载行为

在 Python 中，模块的加载方式有一些有趣的特性。在这一步，我们将探索这些行为，以了解 Python 是如何管理模块加载的。

1. 首先，让我们看看在同一个 Python 解释器会话中再次导入模块时会发生什么。当你启动 Python 解释器时，就像是打开了一个可以运行 Python 代码的工作空间。一旦你导入了一个模块，再次导入它似乎会重新加载该模块，但事实并非如此。

```python
>>> import simplemod
```

注意，这次你没有看到 “Loaded simplemod” 的输出。这是因为 **Python 在每个解释器会话中只加载一次模块**。后续的 `import` 语句不会重新加载模块。Python 会记住它已经加载了该模块，因此不会再次执行加载过程。

2. 导入模块后，你可以修改其中的变量。Python 中的模块就像一个容器，包含变量、函数和类。导入模块后，你可以像处理其他 Python 对象一样访问和更改其变量。

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> simplemod.foo()
x is 13
```

在这里，我们首先检查 `simplemod` 模块中变量 `x` 的值，最初它是 `42`。然后我们将其值更改为 `13` 并验证更改已生效。当我们调用模块中的 `foo` 函数时，它反映了 `x` 的新值。

3. 再次导入模块不会重置我们对其变量所做的更改。即使我们再次尝试导入该模块，Python 也不会重新加载它，因此我们对其变量所做的更改仍然保留。

```python
>>> import simplemod
>>> simplemod.x
13
```

4. 如果你想强制重新加载一个模块，你需要使用 `importlib.reload()` 函数。有时，你可能对模块的代码进行了更改，并希望立即看到这些更改生效。`importlib.reload()` 函数可以帮助你实现这一点。

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
```

模块已被重新加载，`x` 的值已重置为 `42`。这表明模块已从其源代码重新加载，所有变量都已恢复到初始状态。

5. Python 在 `sys.modules` 字典中跟踪所有已加载的模块。这个字典就像一个注册表，Python 会存储当前解释器会话期间加载的所有模块的信息。

```python
>>> 'simplemod' in sys.modules
True
>>> sys.modules['simplemod']
<module 'simplemod' from 'simplemod.py'>
```

通过检查模块名称是否在 `sys.modules` 字典中，你可以查看该模块是否已加载。通过使用模块名称作为键访问该字典，你可以获取有关该模块的信息。

6. 你可以从这个字典中移除一个模块，以强制 Python 在下次导入时重新加载它。如果你从 `sys.modules` 字典中移除一个模块，Python 会忘记它已经加载了该模块。因此，下次你尝试导入它时，Python 将从其源代码重新加载它。

```python
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>> simplemod.x
42
```

该模块被重新加载了，因为它已从 `sys.modules` 中移除。这是确保你使用模块代码的最新版本的另一种方法。
