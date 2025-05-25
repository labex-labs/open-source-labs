# Avaliar o Classificador Random Forest

Vamos avaliar o Classificador Random Forest calculando a taxa de acerto nos dados de teste.

```python
accuracy = random_forest.score(X_test, y_test)
print(f"Precisão do Classificador Random Forest: {accuracy}")
```
