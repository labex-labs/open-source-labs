# Criar o gráfico

Usaremos a função `contourf` para criar um gráfico de contorno preenchido com uma escala de cores logarítmica:

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

cbar = fig.colorbar(cs)

plt.show()
```
