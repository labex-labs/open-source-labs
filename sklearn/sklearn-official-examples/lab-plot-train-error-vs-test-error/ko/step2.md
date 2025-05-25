# 학습 및 테스트 오류 계산

Scikit-learn 의 Elastic-Net 회귀 모델을 사용하여 학습 및 테스트 오류를 계산합니다. 정규화 매개변수 `alpha`를 `np.logspace()`를 사용하여 10^-5 에서 10^1 까지의 범위로 설정합니다. 또한 `l1_ratio`를 0.7 로, `max_iter`를 10000 으로 설정합니다.

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
