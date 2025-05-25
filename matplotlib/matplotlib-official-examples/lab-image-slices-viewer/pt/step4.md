# Criar o gráfico e conectar o evento de rolagem

Criaremos o gráfico usando a função `subplots` do Matplotlib e passaremos o objeto `IndexTracker` criado para ele. Em seguida, conectaremos o evento de rolagem à tela da figura usando `mpl_connect`.

```python
fig, ax = plt.subplots()
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```
