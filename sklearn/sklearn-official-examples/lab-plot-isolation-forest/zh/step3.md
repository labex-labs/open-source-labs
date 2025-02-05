# 训练模型

我们将使用训练数据训练一个隔离森林（Isolation Forest）模型。

```python
from sklearn.ensemble import IsolationForest

clf = IsolationForest(max_samples=100, random_state=0)
clf.fit(X_train)
```
