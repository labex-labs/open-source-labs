# 图的最短路径

## 问题

给定一个带权有向图，找出两个节点之间的最短路径。

## 要求

为了解决这个问题，我们需要考虑以下要求：

- 这是一个有向图吗？ - 是
- 图中可能存在环吗？ - 是
  - 注意：如果答案是否定的，这将是一个有向无环图（DAG）。
    - 有向无环图可以用 [拓扑排序](http://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/) 来解决
- 边有权重吗？ - 是
  - 注意：如果边没有权重，我们可以进行广度优先搜索（BFS）
- 边的权重都是非负数吗？ - 是
  - 注意：带有负边的图可以用贝尔曼 - 福特算法解决
    - 带有负权环的图没有定义好的最短路径
- 我们必须检查非负边吗？ - 否
- 我们可以假设这是一个连通图吗？ - 是
- 我们可以假设输入是有效的吗？ - 否
- 我们可以假设我们已经有一个图类吗？ - 是
- 我们可以假设我们已经有一个优先队列类吗？ - 是
- 我们可以假设这能装入内存吗？ - 是

## 示例

考虑以下图：

```txt
graph.add_edge('a', 'b', weight=5)
graph.add_edge('a', 'c', weight=3)
graph.add_edge('a', 'e', weight=2)
graph.add_edge('b', 'd', weight=2)
graph.add_edge('c', 'b', weight=1)
graph.add_edge('c', 'd', weight=1)
graph.add_edge('d', 'a', weight=1)
graph.add_edge('d', 'g', weight=2)
graph.add_edge('d', 'h', weight=1)
graph.add_edge('e', 'a', weight=1)
graph.add_edge('e', 'h', weight=4)
graph.add_edge('e', 'i', weight=7)
graph.add_edge('f', 'b', weight=3)
graph.add_edge('f', 'g', weight=1)
graph.add_edge('g', 'c', weight=3)
graph.add_edge('g', 'i', weight=2)
graph.add_edge('h', 'c', weight=2)
graph.add_edge('h', 'f', weight=2)
graph.add_edge('h', 'g', weight=2)
```

我们可以使用 `ShortestPath` 类找到节点 'a' 和节点 'i' 之间的最短路径：

```txt
shortest_path = ShortestPath(graph)
result = shortest_path.find_shortest_path('a', 'i')
```

预期结果是：

```txt
['a', 'c', 'd', 'g', 'i']
```

我们也可以检查最短路径的权重：

```txt
self.assertEqual(shortest_path.path_weight['i'], 8)
```
