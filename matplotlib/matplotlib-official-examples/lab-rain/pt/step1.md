# Criar uma nova Figura e Eixos (Axes)

O primeiro passo é criar uma nova figura e eixos (axes) que a preencham. Esta será a tela na qual a simulação será desenhada.

```python
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
```
