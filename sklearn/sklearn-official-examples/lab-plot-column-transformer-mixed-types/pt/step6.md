# Dividir os Dados

Neste passo, dividiremos os nossos dados em conjuntos de treino e teste utilizando `train_test_split`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```
