# 加载数据集

第一步是从 scikit-learn 中加载鸢尾花数据集。

```python
from sklearn.datasets import load_iris

# 加载数据集
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
```
