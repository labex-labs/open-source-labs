# 加载数据

我们将使用 `load_diabetes` 方法从 scikit-learn 中加载糖尿病数据集。

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
```
