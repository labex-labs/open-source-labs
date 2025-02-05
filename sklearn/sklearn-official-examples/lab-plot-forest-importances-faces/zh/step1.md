# 加载数据与模型拟合

我们首先加载 Olivetti Faces 数据集，并将数据集限制为仅包含前五个类别。然后，我们在该数据集上训练一个随机森林，并评估基于杂质的特征重要性。我们将设置用于任务的核心数量。

```python
from sklearn.datasets import fetch_olivetti_faces

# 我们选择用于执行森林模型并行拟合的核心数量。`-1` 表示使用所有可用核心。
n_jobs = -1

# 加载人脸数据集
data = fetch_olivetti_faces()
X, y = data.data, data.target

# 将数据集限制为 5 个类别。
mask = y < 5
X = X[mask]
y = y[mask]

# 将拟合一个随机森林分类器以计算特征重要性。
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=750, n_jobs=n_jobs, random_state=42)

forest.fit(X, y)
```
