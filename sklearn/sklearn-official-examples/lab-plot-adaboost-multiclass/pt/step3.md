# Dividir o Conjunto de Dados

Dividiremos o conjunto de dados em conjuntos de treinamento e teste, utilizando os primeiros 3000 exemplos para treinamento e os exemplos restantes para teste.

```python
n_split = 3000
X_train, X_test = X[:n_split], X[n_split:]
y_train, y_test = y[:n_split], y[n_split:]
```
