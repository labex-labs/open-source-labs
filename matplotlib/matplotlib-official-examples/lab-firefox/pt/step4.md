# Criar o Gráfico

Agora criaremos o gráfico usando Matplotlib, adicionando dois objetos `PathPatch` ao gráfico. Um será uma forma preenchida em laranja, enquanto o outro será um contorno branco.

```python
# Definir os limites do gráfico
xmin, ymin = verts.min(axis=0) - 1
xmax, ymax = verts.max(axis=0) + 1

# Criar o gráfico
fig = plt.figure(figsize=(5, 5), facecolor="0.75")  # gray background
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1,
                  xlim=(xmin, xmax),  # centering
                  ylim=(ymax, ymin),  # centering, upside down
                  xticks=[], yticks=[])  # no ticks

# Adicionar o contorno branco
ax.add_patch(patches.PathPatch(path, facecolor='none', edgecolor='w', lw=6))

# Adicionar a forma laranja
ax.add_patch(patches.PathPatch(path, facecolor='orange', edgecolor='k', lw=2))

# Exibir o gráfico
plt.show()
```
