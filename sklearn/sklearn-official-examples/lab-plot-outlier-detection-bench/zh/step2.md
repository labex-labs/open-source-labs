# 离群点预测函数

下一步是定义一个离群点预测函数。在本示例中，我们使用“局部离群因子（LocalOutlierFactor）”和“孤立森林（IsolationForest）”算法。`compute_prediction`函数返回X的平均离群点分数。

```python
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest

def compute_prediction(X, model_name):
    print(f"Computing {model_name} prediction...")
    if model_name == "LOF":
        clf = LocalOutlierFactor(n_neighbors=20, contamination="auto")
        clf.fit(X)
        y_pred = clf.negative_outlier_factor_
    if model_name == "IForest":
        clf = IsolationForest(random_state=rng, contamination="auto")
        y_pred = clf.fit(X).decision_function(X)
    return y_pred
```
