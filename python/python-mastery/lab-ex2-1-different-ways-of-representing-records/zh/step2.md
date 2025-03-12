# 使用不同存储方法测量内存使用情况

在这一步中，我们将探讨不同的数据存储方式如何影响内存使用。内存使用是编程中的一个重要方面，尤其是在处理大型数据集时。为了测量 Python 代码的内存使用情况，我们将使用 Python 的 `tracemalloc` 模块。这个模块非常有用，因为它允许我们跟踪 Python 进行的内存分配。通过使用它，我们可以了解数据存储方法消耗了多少内存。

## 方法 1：将整个文件存储为单个字符串

让我们先创建一个新的 Python 文件。导航到 `/home/labex/project` 目录并创建一个名为 `memory_test1.py` 的文件。你可以使用文本编辑器打开这个文件。文件打开后，添加以下代码。这段代码将把文件的整个内容作为单个字符串读取，并测量内存使用情况。

```python
# memory_test1.py
import tracemalloc

def test_single_string():
    # 开始跟踪内存
    tracemalloc.start()

    # 将整个文件作为单个字符串读取
    with open('/home/labex/project/ctabus.csv') as f:
        data = f.read()

    # 获取内存使用统计信息
    current, peak = tracemalloc.get_traced_memory()

    print(f"File length: {len(data)} characters")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # 停止跟踪内存
    tracemalloc.stop()

if __name__ == "__main__":
    test_single_string()
```

添加代码后，保存文件。现在，要运行这个脚本，打开终端并执行以下命令：

```bash
python3 /home/labex/project/memory_test1.py
```

运行脚本时，你应该会看到类似以下的输出：

```
File length: 12361039 characters
Current memory usage: 11.80 MB
Peak memory usage: 23.58 MB
```

具体的数字在你的系统上可能会有所不同，但通常你会注意到当前内存使用量约为 12 MB，峰值内存使用量约为 24 MB。

## 方法 2：存储为字符串列表

接下来，我们将测试另一种存储数据的方法。在同一个 `/home/labex/project` 目录下创建一个名为 `memory_test2.py` 的新文件。在编辑器中打开这个文件并添加以下代码。这段代码读取文件并将每行作为一个单独的字符串存储在列表中，然后测量内存使用情况。

```python
# memory_test2.py
import tracemalloc

def test_list_of_strings():
    # 开始跟踪内存
    tracemalloc.start()

    # 将文件读取为字符串列表（每行一个字符串）
    with open('/home/labex/project/ctabus.csv') as f:
        lines = f.readlines()

    # 获取内存使用统计信息
    current, peak = tracemalloc.get_traced_memory()

    print(f"Number of lines: {len(lines)}")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # 停止跟踪内存
    tracemalloc.stop()

if __name__ == "__main__":
    test_list_of_strings()
```

保存文件，然后在终端中使用以下命令运行脚本：

```bash
python3 /home/labex/project/memory_test2.py
```

你应该会看到类似以下的输出：

```
Number of lines: 577564
Current memory usage: 43.70 MB
Peak memory usage: 43.74 MB
```

注意，与之前将数据存储为单个字符串的方法相比，内存使用量显著增加。这是因为列表中的每行都是一个单独的 Python 字符串对象，每个对象都有自己的内存开销。

## 理解内存差异

这两种方法在内存使用上的差异展示了 Python 编程中一个重要的概念，即对象开销。当你将数据存储为字符串列表时，每个字符串都是一个单独的 Python 对象。每个对象都有一些额外的内存需求，包括：

1. Python 对象头（通常每个对象 16 - 24 字节）。这个头包含了对象的相关信息，如类型和引用计数。
2. 实际的字符串表示本身，用于存储字符串的字符。
3. 内存对齐填充。这是为了确保对象的内存地址能够被有效访问而添加的额外空间。

另一方面，当你将整个文件内容存储为单个字符串时，只有一个对象，因此只有一组开销。考虑到数据的总大小，这种方式在内存使用上更高效。

在设计处理大型数据集的程序时，你需要考虑内存效率和数据可访问性之间的权衡。有时，将数据存储为字符串列表可能更便于访问，但会使用更多的内存。而在其他时候，你可能会优先考虑内存效率，选择将数据存储为单个字符串。
