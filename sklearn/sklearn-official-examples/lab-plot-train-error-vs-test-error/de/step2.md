# Trainings- und Testfehler berechnen

Wir werden die Trainings- und Testfehler mit dem Elastic-Net-Regressionsmodell von Scikit-learn berechnen. Wir werden den Regularisierungsparameter `alpha` auf einen Wertebereich von 10^-5 bis 10^1 mit `np.logspace()` setzen. Wir werden auch das `l1_ratio` auf 0,7 und `max_iter` auf 10000 setzen.

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
print("Optimaler Regularisierungsparameter : %s" % alpha_optim)
```
