# Ajustar um Classificador Random Forest

Em seguida, ajustaremos um Classificador Random Forest nos dados de treino. O Classificador Random Forest também é um método de conjunto que utiliza amostragem bootstrap para criar múltiplas árvores de decisão, mas adiciona aleatoriedade extra considerando apenas um subconjunto de características em cada divisão.

```python
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, y_train)
```
