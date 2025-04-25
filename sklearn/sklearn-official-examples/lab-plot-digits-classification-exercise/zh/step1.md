# 加载数字数据集

我们将首先使用 scikit-learn 中的`load_digits`函数加载数字数据集。此函数返回两个数组：包含输入数据的`X_digits`和包含目标标签的`y_digits`。

```python
from sklearn import datasets

X_digits, y_digits = datasets.load_digits(return_X_y=True)
```
