# 使用袋外估计拟合分类器

接下来，我们将使用 `sklearn.ensemble` 模块中的 `GradientBoostingClassifier` 类创建一个带有袋外估计的梯度提升分类器。我们将估计器的数量设置为 100，学习率设置为 0.1。

```python
from sklearn.ensemble import GradientBoostingClassifier

params = {
    "n_estimators": 100,
    "learning_rate": 0.1,
    "subsample": 1.0,
    "max_depth": 3,
    "min_samples_leaf": 1,
    "random_state": 1,
    "oob_score": True
}

clf = GradientBoostingClassifier(**params)
clf.fit(X, y)
```
