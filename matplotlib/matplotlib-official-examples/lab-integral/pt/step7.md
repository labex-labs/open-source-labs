# Adicionar rótulos dos eixos e rótulos de marcação

Adicione os rótulos dos eixos x e y usando `figtext`. Oculte as bordas superior e direita usando `spines`. Defina a colocação e os rótulos de marcação personalizados usando `set_xticks` e `set_yticks`.

```python
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])
```
