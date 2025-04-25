# 确定一组样本的公共节点

对于一组样本，我们可以使用`decision_path`方法和`toarray`方法将指示矩阵转换为密集数组，从而确定这些样本所经过的公共节点。

```python
sample_ids = [0, 1]
# 布尔数组，指示两个样本都经过的节点
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)
# 使用数组中的位置获取节点 ID
common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\n以下样本 {samples} 在树中共享节点 {nodes}。".format(
        samples=sample_ids, nodes=common_node_id
    )
)
print("这占所有节点的 {prop}%。".format(prop=100 * len(common_node_id) / n_nodes))
```
