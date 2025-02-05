# 进行预测

一旦分类器训练完成，我们就可以用它对测试数据进行预测。

```python
# 对测试数据进行预测
y_pred = clf.predict(X_test)

# 打印预测值
print("Predicted values:", y_pred)
```
