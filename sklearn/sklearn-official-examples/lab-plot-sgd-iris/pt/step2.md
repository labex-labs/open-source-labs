# Treinar o Modelo

Agora, treinaremos o modelo `SGDClassifier` no conjunto de dados iris com a ajuda do método `fit()`. Este método recebe os dados de entrada e os valores-alvo como entrada e treina o modelo nos dados fornecidos.

```python
clf = SGDClassifier(alpha=0.001, max_iter=100).fit(X, y)
```
