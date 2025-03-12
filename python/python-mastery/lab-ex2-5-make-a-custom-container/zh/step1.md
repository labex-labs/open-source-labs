# 理解列表的内存分配

在 Python 中，列表是一种非常有用的数据结构，尤其在你需要向其中添加元素时。Python 列表的设计使得追加操作非常高效。Python 不会精确地分配所需的内存量，而是会预先分配额外的内存，以应对未来的元素添加。这种策略可以减少列表增长时所需的内存重新分配次数。

让我们通过使用 `sys.getsizeof()` 函数来更好地理解这个概念。该函数以字节为单位返回对象的大小，这有助于我们了解列表在不同阶段使用了多少内存。

1. 首先，你需要在终端中打开一个 Python 交互式 shell。这就像是一个游乐场，你可以立即运行 Python 代码。要打开它，请在终端中输入以下命令并按回车键：

```bash
python3
```

2. 进入 Python 交互式 shell 后，你需要导入 `sys` 模块。Python 中的模块就像包含有用函数的工具箱。`sys` 模块包含我们需要的 `getsizeof()` 函数。导入模块后，创建一个名为 `items` 的空列表。以下是实现该操作的代码：

```python
import sys
items = []
```

3. 现在，让我们检查空列表的初始大小。我们将使用 `sys.getsizeof()` 函数，并将 `items` 列表作为其参数。在 Python 交互式 shell 中输入以下代码并按回车键：

```python
sys.getsizeof(items)
```

你应该会看到一个类似 `64` 字节的值。这个值代表空列表的开销。开销是指即使列表没有元素，Python 用于管理列表所需的基本内存量。

4. 接下来，我们将开始逐个向列表中添加元素，并观察内存分配的变化。我们将使用 `append()` 方法向列表中添加一个元素，然后再次检查大小。以下是代码：

```python
items.append(1)
sys.getsizeof(items)
```

你应该会看到一个更大的值，大约为 `96` 字节。这个大小的增加表明 Python 已经分配了更多的内存来容纳新元素。

5. 让我们继续向列表中添加更多元素，并在每次添加后检查大小。以下是实现该操作的代码：

```python
items.append(2)
sys.getsizeof(items)  # Size remains the same

items.append(3)
sys.getsizeof(items)  # Size still unchanged

items.append(4)
sys.getsizeof(items)  # Size still unchanged

items.append(5)
sys.getsizeof(items)  # Size jumps to a larger value
```

你会注意到，列表的大小并非每次追加操作都会增加。相反，它会周期性地跳跃式增长。这表明 Python 是以块为单位分配内存的，而不是为每个新元素单独分配内存。

这种行为是经过设计的。Python 最初会分配比所需更多的内存，以避免列表增长时频繁进行重新分配。每当列表超出其当前容量时，Python 会分配更大的一块内存。

请记住，列表存储的是对象的引用，而不是对象本身。在 64 位系统上，每个引用通常需要 8 字节的内存。理解这一点很重要，因为它会影响列表在包含不同类型对象时实际使用的内存量。
