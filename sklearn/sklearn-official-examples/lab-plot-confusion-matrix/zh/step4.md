# 训练模型

我们将使用线性核来训练一个支持向量机（SVM）分类器。我们会使用一个设置得很低的正则化参数C，以便观察其对结果的影响。

```python
classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
```
