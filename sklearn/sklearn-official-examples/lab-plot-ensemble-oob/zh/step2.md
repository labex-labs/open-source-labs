# 生成二元分类数据集

接下来，我们将使用 scikit-learn 提供的 `make_classification` 函数生成一个二元分类数据集。这个函数允许我们指定样本数量、特征数量、每个类别的簇数以及信息性特征的数量。我们将使用固定的随机状态值以确保可重复性。

```python
X, y = make_classification(
    n_samples=500,
    n_features=25,
    n_clusters_per_class=1,
    n_informative=15,
    random_state=RANDOM_STATE,
)
```
