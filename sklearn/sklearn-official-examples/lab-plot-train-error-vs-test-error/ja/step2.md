# 学習誤差とテスト誤差の計算

Scikit-learn の Elastic-Net 回帰モデルを使って学習誤差とテスト誤差を計算します。正則化パラメータ`alpha`を`np.logspace()`を使って 10^-5 から 10^1 の範囲の値に設定します。また、`l1_ratio`を 0.7 に、`max_iter`を 10000 に設定します。

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
