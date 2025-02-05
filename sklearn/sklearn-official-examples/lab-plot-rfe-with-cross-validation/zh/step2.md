# 模型训练与选择

我们将创建RFECV对象并计算交叉验证分数。评分策略“accuracy”（准确率）用于优化正确分类样本的比例。我们将使用逻辑回归作为估计器，并采用5折分层k折交叉验证。

```python
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression

min_features_to_select = 1  # 要考虑的最小特征数量
clf = LogisticRegression()
cv = StratifiedKFold(5)

rfecv = RFECV(
    estimator=clf,
    step=1,
    cv=cv,
    scoring="accuracy",
    min_features_to_select=min_features_to_select,
    n_jobs=2,
)
rfecv.fit(X, y)

print(f"Optimal number of features: {rfecv.n_features_}")
```
