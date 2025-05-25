# Pré-processamento de Dados

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Dividimos o conjunto de dados em um conjunto de treinamento e um conjunto de teste e pré-processamos os dados escalando os dados de entrada usando a função `StandardScaler()`.
