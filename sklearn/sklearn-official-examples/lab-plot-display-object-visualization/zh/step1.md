# 加载数据并训练模型

对于这个示例，我们将使用来自 OpenML 的输血服务中心数据集。目标是判断一个人是否献血。首先，将数据拆分为训练集和测试集，然后使用训练数据集拟合逻辑回归模型。

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=1464, return_X_y=True, parser="pandas")
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

clf = make_pipeline(StandardScaler(), LogisticRegression(random_state=0))
clf.fit(X_train, y_train)
```
