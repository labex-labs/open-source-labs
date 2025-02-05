# 列表增长

Python 列表针对执行 `append()` 操作进行了高度优化。每次列表增长时，它会获取比实际所需更大的一块内存，预期之后会有更多数据添加到列表中。如果添加新项且有可用空间，`append()` 操作会存储该项而无需分配更多内存。

通过对列表使用 `sys.getsizeof()` 函数并追加一些项来试验列表的此特性。

```python
>>> import sys
>>> items = []
>>> sys.getsizeof(items)
64
>>> items.append(1)
>>> sys.getsizeof(items)
96
>>> items.append(2)
>>> sys.getsizeof(items)    # 注意大小如何没有增加
96
>>> items.append(3)
>>> sys.getsizeof(items)    # 这里仍然没有增加
96
>>> items.append(4)
>>> sys.getsizeof(items)    # 还没有。
96
>>> items.append(5)
>>> sys.getsizeof(items)    # 注意大小已经跳跃
128
>>>
```

列表通过引用来存储其项。因此，每个项所需的内存是一个单一的内存地址。在 64 位机器上，一个地址通常是 8 字节。但是，如果 Python 是为 32 位编译的，它可能是 4 字节，并且上述示例中的数字将是所显示数字的一半。
