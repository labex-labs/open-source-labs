# Avaliando o Modelo

Para avaliar o desempenho do nosso modelo, podemos usar a função `accuracy_score` do scikit-learn:

```python
from sklearn.metrics import accuracy_score

# Predizer as etiquetas do conjunto de teste
y_pred = clf.predict(X_test)

# Calcular a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)

# Imprimir a precisão do modelo
print("Precisão:", accuracy)
```
