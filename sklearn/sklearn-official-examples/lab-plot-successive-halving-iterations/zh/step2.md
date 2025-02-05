# 加载数据集

`sklearn.datasets` 模块中的 `make_classification` 函数用于生成一个分类数据集。该数据集包含400个样本和12个特征。加载数据集的代码如下：

```python
rng = np.random.RandomState(0)
X, y = datasets.make_classification(n_samples=400, n_features=12, random_state=rng)
```
