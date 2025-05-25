# Avaliar o modelo

Agora, avaliaremos o modelo treinado usando o conjunto de validação. A métrica de avaliação usada aqui é o coeficiente de determinação (R-quadrado).

```python
# Avaliar o modelo no conjunto de validação
score = model.score(X_val, y_val)
print("Score de validação:", score)
```
