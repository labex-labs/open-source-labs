# Avaliar o Modelo

Finalmente, podemos avaliar a precisão do nosso modelo comparando os valores previstos com os valores reais.

```python
# Calcular a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)

# Imprimir a precisão
print("Precisão:", accuracy)
```
