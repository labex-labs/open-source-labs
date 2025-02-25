# Personalizar el gráfico

Podemos personalizar el gráfico agregando etiquetas, títulos y cambiando la paleta de colores:

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.coolwarm)

ax.set_title('Contourf Plot with Log Color Scale')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')

cbar = fig.colorbar(cs)

plt.show()
```
