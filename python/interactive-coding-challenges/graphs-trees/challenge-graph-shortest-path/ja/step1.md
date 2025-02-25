# グラフの最短経路

## 問題

重み付きの有向グラフが与えられたとき、2つのノード間の最短経路を求める。

## 要件

この問題を解くには、以下の要件を考慮する必要がある。

- これは有向グラフか？ - はい
- グラフにサイクルがあり得るか？ - はい
  - 注：答えが「いいえ」の場合、これはDAGになる。
    - DAGは[トポロジカルソート](http://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/)を使って解くことができる。
- 辺に重みがあるか？ - はい
  - 注：辺に重みがない場合、BFSを行うことができる。
- 辺はすべて非負の数か？ - はい
  - 注：負の辺があるグラフはベルマンフォード法で解くことができる。
    - 負のコストサイクルがあるグラフには定義された最短経路はない。
- 非負の辺をチェックする必要があるか？ - いいえ
- これが連結グラフであると仮定できるか？ - はい
- 入力が有効であると仮定できるか？ - いいえ
- 既にグラフクラスがあると仮定できるか？ - はい
- 既に優先度付きキュークラスがあると仮定できるか？ - はい
- これがメモリに収まると仮定できるか？ - はい

## 例

次のグラフを考える。

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

ShortestPathクラスを使ってノード'a'とノード'i'間の最短経路を求めることができる。

```txt
shortest_path = ShortestPath(graph)
result = shortest_path.find_shortest_path('a', 'i')
```

期待される結果は以下の通り。

```txt
['a', 'c', 'd', 'g', 'i']
```

また、最短経路の重みをチェックすることもできる。

```txt
self.assertEqual(shortest_path.path_weight['i'], 8)
```
