# 评估模型

最后，我们可以通过将预测值与真实值进行比较来评估模型的准确性。

```python
# 计算模型的准确性
accuracy = accuracy_score(y_test, y_pred)

# 打印准确性
print("Accuracy:", accuracy)
```
