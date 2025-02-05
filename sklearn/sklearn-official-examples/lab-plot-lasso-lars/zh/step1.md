# 加载数据

第一步是从 Scikit-Learn 中加载糖尿病数据集。

```python
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
```
