# 第三方测试工具

内置的 `unittest` 模块的优点是随处可用 —— 它是 Python 的一部分。然而，许多程序员也发现它相当冗长。一个流行的替代方案是 [pytest](https://docs.pytest.org/en/latest/)。使用 pytest，你的测试文件可以简化为如下内容：

```python
# test_simple.py
import simple

def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'
```

要运行测试，只需输入类似 `python -m pytest` 的命令。然后它会找到并运行所有测试。可以使用 `pip install pytest` 安装该模块。

`pytest` 的功能远不止于此示例，但如果你决定尝试一下，通常很容易上手。

在本练习中，你将探索使用 Python 的 `unittest` 模块的基本机制。

在之前的练习中，你编写了一个包含 `Stock` 类的 `stock.py` 文件。对于本练习，假设你正在使用为练习 7.9 编写的涉及类型化属性的代码。如果由于某种原因该代码无法正常工作，你可能需要将 `Solutions/7_9` 中的解决方案复制到你的工作目录中。
