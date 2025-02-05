# 预测并评估准确率

我们对输入数据预测类别标签，并评估分类器的准确率。

```python
y_pred = clf.predict(X)
print("Accuracy: ", np.mean(y == y_pred))
```
