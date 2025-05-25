# Criando a Figura e os Eixos

Criaremos o objeto figura e eixos usando a função `subplots()`. Também adicionaremos um patch de círculo amarelo ao objeto eixos usando a função `patches.Circle()`.

```python
fig, ax = plt.subplots()
circ = patches.Circle((0.5, 0.5), 0.25, alpha=0.8, fc='yellow')
ax.add_patch(circ)
```
