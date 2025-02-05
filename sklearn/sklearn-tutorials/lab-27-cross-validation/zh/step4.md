# 训练并评估模型

现在，让我们在训练集上训练一个支持向量机（SVM）分类器，并在测试集上评估其性能。

```python
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Accuracy: ", score)
```
