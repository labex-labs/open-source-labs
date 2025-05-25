# Dividir os Dados em Conjuntos de Treinamento e Teste

Dividiremos nossos dados em um conjunto de treinamento de 400 amostras e um conjunto de teste de 200 amostras usando a função `train_test_split` do scikit-learn.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=400, test_size=200, random_state=4)
```
