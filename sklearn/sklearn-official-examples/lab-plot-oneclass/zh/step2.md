# 拟合单类支持向量机模型

接下来，我们将在生成的数据上拟合单类支持向量机模型。

```python
# 拟合模型
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# 预测训练数据、常规新观测值和异常新观测值的标签
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
```
