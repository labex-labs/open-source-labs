# 定义参数空间

定义一个字典 `param_dist`，其中包含要搜索的超参数及其各自的值。超参数有 `max_depth`、`max_features`、`min_samples_split`、`bootstrap` 和 `criterion`。`max_features` 和 `min_samples_split` 的搜索范围使用 `scipy.stats` 模块中的 `randint` 函数定义。定义参数空间的代码如下：

```python
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 6),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}
```
