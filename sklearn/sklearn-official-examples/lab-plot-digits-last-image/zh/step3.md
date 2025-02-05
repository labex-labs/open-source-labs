# 为机器学习准备数据集

在我们能够在数据集上训练机器学习模型之前，我们需要通过将其拆分为训练集和测试集来准备数据。我们可以使用 scikit-learn 的 `train_test_split` 函数来做到这一点：

```python
from sklearn.model_selection import train_test_split

# 将数据集拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
```
