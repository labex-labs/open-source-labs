# 计算训练误差和测试误差

我们将使用Scikit-learn中的弹性网络回归模型来计算训练误差和测试误差。我们将使用`np.logspace()`把正则化参数`alpha`设置为从10的 -5次方到10的1次方的一系列值。我们还将把`l1_ratio`设置为0.7，把`max_iter`设置为10000。

```python
alphas = np.logspace(-5, 1, 60)
enet = linear_model.ElasticNet(l1_ratio=0.7, max_iter=10000)
train_errors = list()
test_errors = list()
for alpha in alphas:
    enet.set_params(alpha=alpha)
    enet.fit(X_train, y_train)
    train_errors.append(enet.score(X_train, y_train))
    test_errors.append(enet.score(X_test, y_test))

i_alpha_optim = np.argmax(test_errors)
alpha_optim = alphas[i_alpha_optim]
print("Optimal regularization parameter : %s" % alpha_optim)
```
