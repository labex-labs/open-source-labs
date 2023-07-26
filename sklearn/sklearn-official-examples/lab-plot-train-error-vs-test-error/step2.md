# Compute Train and Test Errors

We will compute train and test errors using the Elastic-Net regression model from Scikit-learn. We will set the regularization parameter `alpha` to a range of values from 10^-5 to 10^1 using `np.logspace()`. We will also set the `l1_ratio` to 0.7 and `max_iter` to 10000.

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
