# Определить общие узлы для группы образцов

Для группы образцов мы можем определить общие узлы, через которые проходят образцы, с использованием метода `decision_path` и метода `toarray` для преобразования индикаторной матрицы в плотный массив.

```python
sample_ids = [0, 1]
# boolean array indicating the nodes both samples go through
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)
# obtain node ids using position in array
common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\nThe following samples {samples} share the node(s) {nodes} in the tree.".format(
        samples=sample_ids, nodes=common_node_id
    )
)
print("This is {prop}% of all nodes.".format(prop=100 * len(common_node_id) / n_nodes))
```
