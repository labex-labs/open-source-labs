# Personalizar o gráfico

Podemos personalizar o gráfico adicionando rótulos, títulos e alterando o mapa de cores:

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.coolwarm)

ax.set_title('Contourf Plot with Log Color Scale')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

cbar = fig.colorbar(cs)

plt.show()
```
