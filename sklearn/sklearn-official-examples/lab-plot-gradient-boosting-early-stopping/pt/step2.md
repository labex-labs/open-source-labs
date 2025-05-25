# Preparar os Dados

Em seguida, prepararemos os dados dividindo-os em conjuntos de treino e teste.

```python
for X, y in data_list:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )
```
