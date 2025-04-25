# 评估管道

现在我们将使用`predict`方法在测试子集上评估管道。管道将基于方差分析 F 值选择 3 个最具信息量的特征，并且`LinearSVC`函数将对所选特征进行预测。

```python
from sklearn.metrics import classification_report

y_pred = anova_svm.predict(X_test)
print(classification_report(y_test, y_pred))
```
