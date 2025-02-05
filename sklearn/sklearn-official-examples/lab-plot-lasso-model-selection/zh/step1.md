# 数据集

首先，我们将使用 `sklearn.datasets` 中的 `load_diabetes` 函数加载糖尿病数据集。该数据集由10个基线变量组成，包括年龄、性别、体重指数、平均血压和六项血清测量值，以及基线一年后疾病进展的定量测量值。

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
X.head()
```
