# 探索栈帧检查

我们一直在使用的 `_init(locals())` 方法虽然可行，但有一个缺点。每次定义 `__init__` 方法时，我们都必须显式调用 `locals()`。这可能会有点麻烦，尤其是在处理多个类的时候。幸运的是，我们可以通过使用栈帧检查来让代码更简洁、更高效。这种技术允许我们自动访问调用者的局部变量，而无需显式调用 `locals()`。

让我们在 Python 解释器中开始探索这种技术。首先，打开终端并导航到项目目录。然后，启动 Python 解释器。你可以通过运行以下命令来完成：

```bash
cd ~/project
python3
```

现在我们已经进入 Python 解释器，需要导入 `sys` 模块。`sys` 模块提供了对 Python 解释器使用或维护的一些变量的访问。我们将使用它来访问栈帧信息。

```python
import sys
```

接下来，我们将定义一个改进版的 `_init()` 函数。这个新版本将直接访问调用者的帧，从而无需显式传递 `locals()`。

```python
def _init():
    # Get the caller's frame (1 level up in the call stack)
    frame = sys._getframe(1)

    # Get the local variables from that frame
    locs = frame.f_locals

    # Extract self and set other variables as attributes
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)
```

在这段代码中，`sys._getframe(1)` 会获取调用函数的帧对象。参数 `1` 表示我们要在调用栈中向上查找一层。一旦我们获得了帧对象，就可以使用 `frame.f_locals` 访问其局部变量。这会给我们一个包含调用者作用域中所有局部变量的字典。然后，我们提取 `self` 变量，并将其余变量设置为 `self` 对象的属性。

现在，让我们用新版本的 `Stock` 类来测试这个新的 `_init()` 函数。

```python
class Stock:
    def __init__(self, name, shares, price):
        _init()  # No need to pass locals() anymore!

# Test it
s = Stock('GOOG', 100, 490.1)
print(s.name, s.shares, s.price)

# Also works with keyword arguments
s = Stock(name='AAPL', shares=50, price=125.3)
print(s.name, s.shares, s.price)
```

如你所见，`__init__` 方法不再需要显式传递 `locals()` 了。从调用者的角度来看，这让我们的代码更简洁、更易读。

### 栈帧检查的工作原理

当你调用 `sys._getframe(1)` 时，Python 会返回表示调用者执行帧的帧对象。参数 `1` 表示“从当前帧向上一层”（即调用函数）。

帧对象包含有关执行上下文的重要信息。这包括当前正在执行的函数、该函数中的局部变量以及当前正在执行的行号。

通过访问 `frame.f_locals`，我们可以获得调用者作用域中所有局部变量的字典。这与直接在该作用域中调用 `locals()` 返回的结果类似。

这种技术非常强大，但使用时需要谨慎。它通常被认为是 Python 的高级特性，可能会显得有点“神奇”，因为它超出了 Python 正常的作用域边界。

当你完成栈帧检查的实验后，可以运行以下命令退出 Python 解释器：

```python
exit()
```
