# Criar Contorno Preenchido com Níveis Automáticos

Em seguida, criaremos um gráfico de contorno preenchido com níveis automáticos. Usaremos o método `contourf` com o parâmetro `cmap` definido como `plt.cm.bone` para especificar o mapa de cores (colormap). Também adicionaremos linhas de contorno com o método `contour` e passaremos um subconjunto dos níveis de contorno usados para os contornos preenchidos.

```python
# Create filled contour with automatic levels
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
CS2 = ax.contour(CS, levels=CS.levels[::2], colors='r', origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Automatic Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')
cbar.add_lines(CS2)

# Show plot
plt.show()
```
