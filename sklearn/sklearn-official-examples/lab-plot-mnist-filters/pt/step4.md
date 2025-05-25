# Dividir Dados

Dividiremos o conjunto de dados em um conjunto de treinamento e um conjunto de teste usando a função `train_test_split`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.7)
```
