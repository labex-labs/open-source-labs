# Alterar a orientação do gráfico

Nesta etapa, alteraremos a orientação do gráfico usando o parâmetro `orientation`. Definiremos a orientação como `'x'` para que as hastes sejam projetadas ao longo da direção x e a linha de base (baseline) esteja no plano yz.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()
```
