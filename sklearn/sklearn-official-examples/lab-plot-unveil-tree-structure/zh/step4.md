# 获取决策路径和叶节点

我们可以使用`decision_path`方法来获取感兴趣样本的决策路径。此方法输出一个指示矩阵，通过它我们能够获取感兴趣样本所遍历的节点。感兴趣样本到达的叶节点ID可以通过`apply`方法获得。这将返回每个感兴趣样本到达的叶节点的节点ID数组。利用叶节点ID和`decision_path`，我们可以获得用于预测一个样本或一组样本的分裂条件。以下是获取单个样本的决策路径和叶节点的代码：

```python
node_indicator = clf.decision_path(X_test)
leaf_id = clf.apply(X_test)

sample_id = 0
# 获取样本`sample_id`所经过的节点ID，即行`sample_id`
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print("用于预测样本 {id} 的规则:\n".format(id=sample_id))
for node_id in node_index:
    # 如果是叶节点，则继续到下一个节点
    if leaf_id[sample_id] == node_id:
        continue

    # 检查样本0的分裂特征值是否低于阈值
    if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "决策节点 {node} : (X_test[{sample}, {feature}] = {value}) "
        "{inequality} {threshold})".format(
            node=node_id,
            sample=sample_id,
            feature=feature[node_id],
            value=X_test[sample_id, feature[node_id]],
            inequality=threshold_sign,
            threshold=threshold[node_id],
        )
    )
```
