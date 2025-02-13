# 无权图的图最短路径

## 问题

给定一个没有边权重的有向图，找到两个节点之间的最短路径。

## 要求

要解决此问题，必须满足以下要求：

- 图是有向的。
- 图是无权的。
- 图类和节点类已经可用。
- 输入是两个节点。
- 输出是构成最短路径的节点键列表。
- 如果没有路径，则返回 None。
- 图是连通的。
- 输入是有效的。
- 算法必须适合内存。

## 示例用法

假设我们有以下图：

```
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(0, 5)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 1)
graph.add_edge(3, 2)
graph.add_edge(3, 4)
```

我们可以使用 `search_path` 函数找到两个节点之间的最短路径：

- `search_path(start=0, end=2) -> [0, 1, 3, 2]`
- `search_path(start=0, end=0) -> [0]`
- `search_path(start=4, end=5) -> None`
