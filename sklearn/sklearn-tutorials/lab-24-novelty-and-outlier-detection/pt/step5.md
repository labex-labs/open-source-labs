# Prever valores discrepantes

Depois de o modelo ser ajustado, podemos usar o método `predict` para prever se novas observações são valores discrepantes ou não. O método `predict` retorna 1 para pontos dentro do padrão e -1 para valores discrepantes.

```python
X_test = [5.5, 8.5]
predictions = estimator.predict(X_test)
print(predictions)
```
