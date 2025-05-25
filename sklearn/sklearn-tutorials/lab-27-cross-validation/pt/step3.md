# Dividir o conjunto de dados em conjuntos de treino e teste

Para avaliar o desempenho do nosso modelo, precisamos dividir o conjunto de dados em um conjunto de treino e um conjunto de teste. Usaremos a função `train_test_split` da biblioteca scikit-learn para fazer isso.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
