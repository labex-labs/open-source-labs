# 加载并准备数据

首先，我们将加载糖尿病数据集并为建模做准备。我们将使用scikit-learn中的`load_diabetes`函数将数据集加载到两个数组`X`和`y`中。

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True)
```
