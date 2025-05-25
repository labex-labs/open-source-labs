# Criar um gráfico pcolor

Criaremos um gráfico pcolor usando `ax.tricontourf` e `fig.colorbar`.

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tcf = ax1.tricontourf(triang, z)
fig1.colorbar(tcf)
ax1.tricontour(triang, z, colors='k')
ax1.set_title('Gráfico de contorno da triangulação de Delaunay')
```
