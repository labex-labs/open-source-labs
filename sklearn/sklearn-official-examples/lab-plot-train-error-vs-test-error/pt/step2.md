# Calcular Erros de Treino e Teste

Vamos calcular os erros de treino e teste utilizando o modelo de regressão Elastic-Net do Scikit-learn. Definiremos o parâmetro de regularização `alpha` numa gama de valores de 10^-5 a 10^1 usando `np.logspace()`. Também definiremos o `l1_ratio` para 0,7 e `max_iter` para 10000.

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
print("Parâmetro de regularização ótimo : %s" % alpha_optim)
```
