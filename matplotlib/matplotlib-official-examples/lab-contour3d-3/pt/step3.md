# Plotar a superfície 3D

Nesta etapa, plotaremos a superfície 3D com os dados de teste e personalizaremos a aparência do gráfico.

```python
# Plotar a superfície 3D
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)

# Personalizar a aparência do gráfico
ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100), xlabel='X', ylabel='Y', zlabel='Z')
```
