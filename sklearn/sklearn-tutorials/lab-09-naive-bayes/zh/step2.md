# 将数据集拆分为训练集和测试集

接下来，我们将使用 `sklearn.model_selection` 模块中的 `train_test_split` 函数将数据集拆分为训练集和测试集。训练集将用于训练朴素贝叶斯分类器，测试集将用于评估其性能。

```python
from sklearn.model_selection import train_test_split

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
