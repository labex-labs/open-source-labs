# Dividir Dados

Dividiremos o conjunto de dados em um conjunto de treinamento e um conjunto de teste. O conjunto de treinamento será usado para treinar o classificador SGD, enquanto o conjunto de teste será usado para avaliar seu desempenho.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
