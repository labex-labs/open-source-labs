# 定义参数

我们将为梯度提升分类器定义参数。我们将使用以下参数：

- n_estimators：要执行的提升阶段数
- max_leaf_nodes：每棵树中最大的叶节点数
- max_depth：树的最大深度
- random_state：用于一致性的随机种子
- min_samples_split：拆分内部节点所需的最小样本数

```python
original_params = {
    "n_estimators": 400,
    "max_leaf_nodes": 4,
    "max_depth": None,
    "random_state": 2,
    "min_samples_split": 5,
}
```
