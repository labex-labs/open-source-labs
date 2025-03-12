# 创建自定义描述符

在这一步中，我们将创建自己的描述符类。但首先，让我们了解一下什么是描述符。描述符是实现了描述符协议的 Python 对象，该协议由 `__get__`、`__set__` 和 `__delete__` 方法组成。这些方法允许描述符管理属性的访问、设置和删除方式。通过创建自己的描述符类，我们可以更好地理解这个协议的工作原理。

在项目目录中创建一个名为 `descrip.py` 的新文件。这个文件将包含我们的自定义描述符类。以下是代码：

```python
# descrip.py

class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f'{self.name}:__get__')
        # In a real descriptor, you would return a value here

    def __set__(self, instance, value):
        print(f'{self.name}:__set__ {value}')
        # In a real descriptor, you would store the value here

    def __delete__(self, instance):
        print(f'{self.name}:__delete__')
        # In a real descriptor, you would delete the value here
```

在 `Descriptor` 类中，`__init__` 方法使用一个名称来初始化描述符。当访问属性时会调用 `__get__` 方法，当设置属性时会调用 `__set__` 方法，当删除属性时会调用 `__delete__` 方法。

现在，让我们创建一个测试文件来试验我们的自定义描述符。这将帮助我们了解描述符在不同场景下的行为。创建一个名为 `test_descrip.py` 的文件，代码如下：

```python
# test_descrip.py

from descrip import Descriptor

class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

# Create an instance and try accessing the attributes
if __name__ == '__main__':
    f = Foo()
    print("Accessing attribute f.a:")
    f.a

    print("\nAccessing attribute f.b:")
    f.b

    print("\nSetting attribute f.a = 23:")
    f.a = 23

    print("\nDeleting attribute f.a:")
    del f.a
```

在 `test_descrip.py` 文件中，我们从 `descrip.py` 导入 `Descriptor` 类。然后我们创建一个 `Foo` 类，它有三个属性 `a`、`b` 和 `c`，每个属性都由一个描述符管理。我们创建一个 `Foo` 类的实例，并执行访问、设置和删除属性等操作，以查看描述符方法是如何被调用的。

现在让我们运行这个测试文件，看看描述符是如何工作的。打开你的终端，导航到项目目录，并使用以下命令运行测试文件：

```bash
cd ~/project
python3 test_descrip.py
```

你应该会看到如下输出：

```
Accessing attribute f.a:
a:__get__

Accessing attribute f.b:
b:__get__

Setting attribute f.a = 23:
a:__set__ 23

Deleting attribute f.a:
a:__delete__
```

如你所见，每次你访问、设置或删除由描述符管理的属性时，相应的魔术方法（`__get__`、`__set__` 或 `__delete__`）都会被调用。

让我们也以交互式的方式检查我们的描述符。这将允许我们实时测试描述符并立即看到结果。打开你的终端，导航到项目目录，并使用 `descrip.py` 文件启动一个交互式 Python 会话：

```bash
cd ~/project
python3 -i descrip.py
```

现在在交互式 Python 会话中输入以下命令，看看描述符协议是如何工作的：

```python
class Foo:
    a = Descriptor('a')
    b = Descriptor('b')
    c = Descriptor('c')

f = Foo()
f.a         # Should call __get__
f.b         # Should call __get__
f.a = 23    # Should call __set__
del f.a     # Should call __delete__
exit()
```

这里的关键要点是，描述符提供了一种拦截和自定义属性访问的方式。这使得它们在实现数据验证、计算属性和其他高级行为方面非常强大。通过使用描述符，你可以更好地控制类属性的访问、设置和删除方式。
