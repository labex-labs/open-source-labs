# 创建你的第一个单元测试

Python 的 `unittest` 模块是一个强大的工具，它提供了一种结构化的方式来组织和执行测试。在我们开始编写第一个单元测试之前，让我们先了解一些关键概念。测试固件（Test fixtures）是像 `setUp` 和 `tearDown` 这样的方法，它们有助于在测试前准备环境，并在测试后清理环境。测试用例（Test cases）是单独的测试单元，测试套件（Test suites）是测试用例的集合，而测试运行器（Test runners）负责执行这些测试并展示结果。

在这第一步中，我们将为 `Stock` 类创建一个基本的测试文件，该类已经在 `stock.py` 文件中定义好了。

1. 首先，让我们打开 `stock.py` 文件。这将帮助我们了解要测试的 `Stock` 类。通过查看 `stock.py` 中的代码，我们可以了解该类的结构、它有哪些属性以及提供了哪些方法。要查看 `stock.py` 文件的内容，请在终端中运行以下命令：

```bash
cat stock.py
```

2. 现在，是时候使用你喜欢的文本编辑器创建一个名为 `teststock.py` 的新文件了。这个文件将包含我们针对 `Stock` 类的测试用例。以下是你需要在 `teststock.py` 文件中编写的代码：

```python
# teststock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

让我们来分析一下这段代码的关键部分：

- `import unittest`：这行代码导入了 `unittest` 模块，该模块为在 Python 中编写和运行测试提供了必要的工具和类。
- `import stock`：这行代码导入了包含我们 `Stock` 类的模块。如果没有这个导入，我们就无法在测试代码中访问 `Stock` 类。
- `class TestStock(unittest.TestCase)`：我们创建了一个名为 `TestStock` 的新类，它继承自 `unittest.TestCase`。这使得我们的 `TestStock` 类成为一个测试用例类，它可以包含多个测试方法。
- `def test_create(self)`：这是一个测试方法。在 `unittest` 框架中，所有的测试方法都必须以 `test_` 作为前缀。这个方法创建了一个 `Stock` 类的实例，然后使用 `assertEqual` 方法来检查 `Stock` 实例的属性是否与预期值匹配。
- `assertEqual`：这是 `TestCase` 类提供的一个方法。它用于检查两个值是否相等。如果它们不相等，测试将失败。
- `unittest.main()`：当直接执行这个脚本时，`unittest.main()` 将运行 `TestStock` 类中的所有测试方法并显示结果。

3. 在 `teststock.py` 文件中编写完代码后，保存它。然后，在终端中运行以下命令来执行测试：

```bash
python3 teststock.py
```

你应该会看到类似于以下的输出：

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

输出中的单个点 (`.`) 表示一个测试已成功通过。如果测试失败，你将看到一个 `F` 而不是点，同时还会有关于测试中出现问题的详细信息。这个输出有助于你快速确定你的代码是否按预期工作，或者是否有需要修复的问题。
