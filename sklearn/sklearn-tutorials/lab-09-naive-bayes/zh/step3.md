# 训练并评估高斯朴素贝叶斯分类器

现在，我们将在训练集上训练高斯朴素贝叶斯分类器，并在测试集上评估其性能。我们将使用 `sklearn.naive_bayes` 模块中的 `GaussianNB` 类。

```python
from sklearn.naive_bayes import GaussianNB

# 创建一个高斯朴素贝叶斯分类器
gnb = GaussianNB()

# 训练分类器
gnb.fit(X_train, y_train)

# 预测测试集的目标变量
y_pred = gnb.predict(X_test)

# 计算分类器的准确率
accuracy = (y_pred == y_test).sum() / len(y_test)
print("准确率：", accuracy)
```
