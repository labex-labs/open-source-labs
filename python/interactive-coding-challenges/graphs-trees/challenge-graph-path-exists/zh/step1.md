# 图中路径是否存在

## 问题

给定一个有向图和两个节点，编写一个 Python 函数来确定这两个节点之间是否存在路径。

## 要求

为了解决这个问题，我们需要做出以下假设：

- 图是有向的。
- 我们已经有了图（Graph）和节点（Node）类。
- 图是连通的。
- 输入是有效的。
- 解决方案符合内存要求。

## 示例用法

假设我们有以下图：

```
graph.add_edge(0, 1, 5)
graph.add_edge(0, 4, 3)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 3, 5)
graph.add_edge(1, 4, 4)
graph.add_edge(2, 1, 6)
graph.add_edge(3, 2, 7)
graph.add_edge(3, 4, 8)
```

我们可以使用以下函数来确定两个节点之间是否存在路径：

```
search_path(start=0, end=2) -> True
search_path(start=0, end=0) -> True
search_path(start=4, end=5) -> False
```

前两个函数调用返回 True，因为起始节点和结束节点之间存在路径。最后一个函数调用返回 False，因为起始节点和结束节点之间不存在路径。
