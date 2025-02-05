# 分析二叉树结构

决策树分类器有一个名为`tree_`的属性，通过它可以访问一些底层属性，比如`node_count`（节点总数）和`max_depth`（树的最大深度）。它还存储了整个二叉树结构，以多个并行数组的形式表示。利用这些数组，我们可以遍历树结构来计算各种属性，比如每个节点的深度以及它是否为叶节点。以下是计算这些属性的代码：

```python
import numpy as np

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, 0)]  # 从根节点ID（0）及其深度（0）开始
while len(stack) > 0:
    # `pop`操作确保每个节点只被访问一次
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # 如果一个节点的左子节点和右子节点不同，那么它就是一个分裂节点
    is_split_node = children_left[node_id]!= children_right[node_id]
    # 如果是分裂节点，将左子节点、右子节点及其深度添加到`stack`中
    # 以便我们可以遍历它们
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True

print(
    "The binary tree structure has {n} nodes and has "
    "the following tree structure:\n".format(n=n_nodes)
)
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}node={node} is a leaf node.".format(
                space=node_depth[i] * "\t", node=i
            )
        )
    else:
        print(
            "{space}node={node} is a split node: "
            "go to node {left} if X[:, {feature}] <= {threshold} "
            "else to node {right}.".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=feature[i],
                threshold=threshold[i],
                right=children_right[i],
            )
        )
```
