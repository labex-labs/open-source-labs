# 拟合单类支持向量机（OneClassSVM）

在这一步中，我们将把单类支持向量机（OneClassSVM）模型拟合到训练数据上。我们将对特征进行标准化处理，然后将 OneClassSVM 模型拟合到训练数据上。

```python
# 标准化特征
mean = BV_bunch.cov_train.mean(axis=0)
std = BV_bunch.cov_train.std(axis=0)
train_cover_std = (BV_bunch.cov_train - mean) / std

# 拟合 OneClassSVM
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.5)
clf.fit(train_cover_std)
```
