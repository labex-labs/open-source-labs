# 创建一个减半随机搜索对象

创建一个 `HalvingRandomSearchCV` 对象，用于在参数空间中进行搜索。该对象接受以下参数：

- `estimator`：要优化的估计器
- `param_distributions`：要搜索的参数空间
- `factor`：每次迭代中候选数量减少的因子
- `random_state`：用于搜索的随机状态

创建该对象的代码如下：

```python
clf = RandomForestClassifier(n_estimators=20, random_state=rng)
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
```
