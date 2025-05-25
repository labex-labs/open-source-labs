# Dividir o Conjunto de Dados

Em seguida, dividimos o conjunto de dados em conjuntos de treino e teste. Usaremos 80% dos dados para treino e 20% para teste.

```python
# Dividir os dados em conjuntos de treino/teste
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Dividir os alvos em conjuntos de treino/teste
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```
