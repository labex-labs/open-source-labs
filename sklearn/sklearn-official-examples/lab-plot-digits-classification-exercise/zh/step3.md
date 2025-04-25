# 将数据集拆分为训练集和测试集

接下来，我们将使用 scikit-learn 的`train_test_split`函数将数据集拆分为训练集和测试集。我们将使用 90% 的数据进行训练，10% 的数据进行测试。

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
```
