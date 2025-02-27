# Calculer les erreurs d'entraînement et de test

Nous allons calculer les erreurs d'entraînement et de test à l'aide du modèle de régression Elastic-Net de Scikit-learn. Nous allons définir le paramètre de régularisation `alpha` sur une plage de valeurs allant de 10^-5 à 10^1 à l'aide de `np.logspace()`. Nous allons également définir `l1_ratio` sur 0,7 et `max_iter` sur 10000.

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
