# 典型相关分析（CCA）（具有对称收缩的PLS模式B）

我们使用典型相关分析（CCA）算法对数据进行变换。

```python
cca = CCA(n_components=2)
cca.fit(X_train, Y_train)
X_train_r, Y_train_r = cca.transform(X_train, Y_train)
X_test_r, Y_test_r = cca.transform(X_test, Y_test)
```
