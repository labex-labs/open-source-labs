# Dividir o Conjunto de Dados

Vamos dividir o conjunto de dados em subconjuntos de treino e teste de 50% cada, utilizando o método `train_test_split()` da biblioteca `sklearn.model_selection`.

```python
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
```
