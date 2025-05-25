# Eixos Quadrados Compartilhados

Produziremos subplots compartilhados que são quadrados em tamanho.

```python
fig2, (ax, ax2) = plt.subplots(ncols=2, sharey=True)

ax.plot([1, 5], [0, 10])
ax2.plot([100, 500], [10, 15])

ax.set_box_aspect(1)
ax2.set_box_aspect(1)

plt.show()
```
