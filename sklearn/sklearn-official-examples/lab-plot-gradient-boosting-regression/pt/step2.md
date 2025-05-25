# Pré-processamento de Dados

Em seguida, dividiremos nosso conjunto de dados para usar 90% para treinamento e deixar o restante para teste. Também definiremos os parâmetros do modelo de regressão.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=13)

params = {
    "n_estimators": 500,
    "max_depth": 4,
    "min_samples_split": 5,
    "learning_rate": 0.01,
    "loss": "squared_error",
}
```
