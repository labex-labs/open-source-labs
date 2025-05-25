# Dividir Dados

Dividiremos o conjunto de dados em um conjunto de treinamento e um conjunto de teste. O conjunto de treinamento será usado para treinar o modelo, e o conjunto de teste será usado para avaliar o desempenho do modelo.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
