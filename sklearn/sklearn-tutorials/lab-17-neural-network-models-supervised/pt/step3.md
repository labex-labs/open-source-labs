# Criar e treinar o modelo MLP

```python
# Criar um classificador MLP com uma camada oculta de 5 neurónios
clf = MLPClassifier(hidden_layer_sizes=(5,), random_state=1)

# Treinar o modelo usando os dados de treino
clf.fit(X, y)
```
