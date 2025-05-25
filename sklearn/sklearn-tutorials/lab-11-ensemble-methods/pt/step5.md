# Avaliar o Classificador Bagging

Vamos avaliar o Classificador Bagging calculando a taxa de acerto nos dados de teste usando o método `score`.

```python
accuracy = bagging.score(X_test, y_test)
print(f"Precisão do Classificador Bagging: {accuracy}")
```
