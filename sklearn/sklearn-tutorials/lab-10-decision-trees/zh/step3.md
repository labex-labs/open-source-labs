# 划分数据集

在训练决策树分类器之前，我们需要将数据集划分为训练集和测试集。我们将使用70%的数据进行训练，30%的数据进行测试。

```python
# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```
