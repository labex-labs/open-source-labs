# Preprocesamiento de datos

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Dividimos el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba y preprocesamos los datos escalando los datos de entrada utilizando la función `StandardScaler()`.
