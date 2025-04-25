# 评估 Bagging 分类器

让我们通过使用`score`方法计算测试数据上的准确率得分来评估 Bagging 分类器。

```python
accuracy = bagging.score(X_test, y_test)
print(f"Bagging Classifier Accuracy: {accuracy}")
```
