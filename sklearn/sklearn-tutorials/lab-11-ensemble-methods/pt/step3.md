# Dividir os Dados

Vamos dividir os dados em conjuntos de treino e teste usando a função `train_test_split` do scikit-learn.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
