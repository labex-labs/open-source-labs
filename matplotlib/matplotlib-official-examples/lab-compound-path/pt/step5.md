# Criando o Gráfico (Plot)

Criaremos o gráfico (plot) e adicionaremos o `PathPatch` ao gráfico. Definiremos o título do gráfico como `'A Compound Path'`.

```python
fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A Compound Path')

ax.autoscale_view()

plt.show()
```
