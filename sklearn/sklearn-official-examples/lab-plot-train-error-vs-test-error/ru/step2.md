# Вычисление ошибок на тренировочных и тестовых данных

Мы вычислим ошибки на тренировочных и тестовых данных с использованием модели регрессии Elastic-Net из Scikit-learn. Мы установим параметр регуляризации `alpha` в диапазон значений от 10^-5 до 10^1 с использованием `np.logspace()`. Мы также установим `l1_ratio` в 0,7 и `max_iter` в 10000.

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
