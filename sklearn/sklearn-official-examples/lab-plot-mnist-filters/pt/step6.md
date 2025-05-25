# Avaliar o Modelo

Avaliaremos o MLPClassifier calculando sua precisão nos conjuntos de treinamento e teste.

```python
print("Score do conjunto de treinamento: %f" % mlp.score(X_train, y_train))
print("Score do conjunto de teste: %f" % mlp.score(X_test, y_test))
```
