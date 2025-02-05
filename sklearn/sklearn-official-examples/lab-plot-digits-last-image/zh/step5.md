# 评估模型

为了评估我们模型的性能，我们可以使用 scikit-learn 的 `accuracy_score` 函数：

```python
from sklearn.metrics import accuracy_score

# 预测测试集的标签
y_pred = clf.predict(X_test)

# 计算模型的准确率
accuracy = accuracy_score(y_test, y_pred)

# 打印模型的准确率
print("Accuracy:", accuracy)
```
