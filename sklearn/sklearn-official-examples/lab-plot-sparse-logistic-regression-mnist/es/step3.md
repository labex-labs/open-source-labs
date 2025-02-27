# Preprocesamiento

Preprocesaremos los datos mezclando los datos, dividiendo el conjunto de datos en conjuntos de entrenamiento y prueba y escalando los datos usando `StandardScaler`.

```python
random_state = check_random_state(0)
permutación = random_state.permutación(X.shape[0])
X = X[permutación]
y = y[permutación]
X = X.reshape((X.shape[0], -1))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=train_samples, test_size=10000
)

escalador = StandardScaler()
X_train = escalador.fit_transform(X_train)
X_test = escalador.transform(X_test)
```
