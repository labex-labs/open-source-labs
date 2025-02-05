# 加载鸢尾花数据集

首先，我们将把鸢尾花数据集加载为一个DataFrame，以演示`set_output` API。

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(as_frame=True, return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
X_train.head()
```
