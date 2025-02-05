# 评估性能

最后，我们将通过计算分类器在测试集上预测的准确率来评估其性能。

```python
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```
