# 拟合一类支持向量机

我们首先将使用带有径向基函数（RBF）核的一类支持向量机对我们的数据集进行拟合。

```python
# 一类支持向量机超参数
nu = 0.05
gamma = 2.0

# 拟合一类支持向量机
clf = OneClassSVM(gamma=gamma, kernel="rbf", nu=nu)
clf.fit(X_train)
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size

Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
```
