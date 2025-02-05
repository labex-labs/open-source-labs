# 加载数据并训练支持向量分类器（SVC）

我们将首先加载葡萄酒数据集，并将其转换为一个二分类问题。然后，我们将在训练数据集上训练一个支持向量分类器。

```python
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import RocCurveDisplay
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

X, y = load_wine(return_X_y=True)
y = y == 2

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
svc = SVC(random_state=42)
svc.fit(X_train, y_train)
```
