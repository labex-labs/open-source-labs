# 二分木構造を分析する

決定木分類器には、`tree_`と呼ばれる属性があり、これを使うと`node_count`（ノードの総数）や`max_depth`（木の最大深さ）などの低レベルの属性にアクセスできます。また、二分木構造全体を多数の並列配列で表現して保存しています。これらの配列を使って、木構造を巡回して各ノードの深さや葉ノードかどうかなどのさまざまなプロパティを計算できます。以下はこれらのプロパティを計算するコードです。

```python
import numpy as np

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, 0)]  # 根ノードID(0)とその深さ(0)で始める
while len(stack) > 0:
    # `pop`により、各ノードが1回だけ訪問されるようにする
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # ノードの左と右の子が同じでなければ、分割ノードである
    is_split_node = children_left[node_id]!= children_right[node_id]
    # 分割ノードの場合、左と右の子と深さを`stack`に追加して、それらをループできるようにする
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True

print(
    "二分木構造は{n}個のノードを持ち、以下の木構造を持っています:\n".format(n=n_nodes)
)
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}node={node}は葉ノードです。".format(
                space=node_depth[i] * "\t", node=i
            )
        )
    else:
        print(
            "{space}node={node}は分割ノードです: "
            "X[:, {feature}] <= {threshold}の場合、ノード{left}に移動し、そうでなければノード{right}に移動します。".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=feature[i],
                threshold=threshold[i],
                right=children_right[i],
            )
        )
```
