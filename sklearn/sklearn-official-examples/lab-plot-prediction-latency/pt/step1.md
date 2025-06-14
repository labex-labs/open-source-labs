# Gerar um Conjunto de Dados de Regressão

Vamos gerar um conjunto de dados de regressão com os parâmetros fornecidos usando a função `make_regression` do Scikit-Learn. O conjunto de dados terá `n_train` instâncias de treino, `n_test` instâncias de teste, `n_features` características e um ruído (noise) de 0,1.

```python
X, y, coef = make_regression(
    n_samples=n_train + n_test, n_features=n_features, noise=noise, coef=True
)

random_seed = 13
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_train, test_size=n_test, random_state=random_seed
)
X_train, y_train = shuffle(X_train, y_train, random_state=random_seed)

X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

y_scaler = StandardScaler()
y_train = y_scaler.fit_transform(y_train[:, None])[:, 0]
y_test = y_scaler.transform(y_test[:, None])[:, 0]
```
