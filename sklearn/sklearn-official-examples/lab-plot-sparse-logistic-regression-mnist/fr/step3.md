# Prétraitement

Nous allons prétraiter les données en les mélangeant, en divisant l'ensemble de données en ensembles d'entraînement et de test, et en mettant à l'échelle les données à l'aide de `StandardScaler`.

```python
random_state = check_random_state(0)
permutation = random_state.permutation(X.shape[0])
X = X[permutation]
y = y[permutation]
X = X.reshape((X.shape[0], -1))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=train_samples, test_size=10000
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
