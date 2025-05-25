# Ajustar um Classificador Bagging

Agora, ajustaremos um Classificador Bagging nos dados de treino. O Classificador Bagging é um método de conjunto que utiliza amostragem bootstrap para criar múltiplos modelos base (geralmente árvores de decisão) e agrega suas previsões usando votação por maioria.

```python
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X_train, y_train)
```
