# 改进模型

如果我们模型的准确率不尽人意，我们可以尝试通过调整支持向量机（SVM）算法的超参数来改进它。例如，我们可以尝试更改 `C` 参数的值：

```python
# 使用不同的C值创建SVM分类器
clf = SVC(kernel='linear', C=0.1)

# 使用训练数据训练分类器
clf.fit(X_train, y_train)

# 预测测试集的标签
y_pred = clf.predict(X_test)

# 计算模型的准确率
accuracy = accuracy_score(y_test, y_pred)

# 打印模型的准确率
print("Accuracy:", accuracy)
```
