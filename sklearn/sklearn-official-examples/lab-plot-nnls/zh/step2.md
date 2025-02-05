# 将数据拆分为训练集和测试集

我们会将数据拆分为训练集和测试集，每个集合各占 50%的数据。

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
```
