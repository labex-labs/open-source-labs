# Criando uma figura e definindo o fundo

Criaremos uma figura usando o método `plt.figure()`, que cria uma instância de `matplotlib.figure.Figure`. Definiremos a cor de fundo da figura usando o método `rect.set_facecolor()`.

```python
fig = plt.figure()
rect = fig.patch  # a rectangle instance
rect.set_facecolor('lightgoldenrodyellow')
```
