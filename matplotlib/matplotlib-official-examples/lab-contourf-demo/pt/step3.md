# Criar Contorno Preenchido com Níveis Explícitos

Agora, criaremos um gráfico de contorno preenchido com níveis explícitos. Usaremos o método `contourf` com o parâmetro `levels` definido como uma lista de valores para especificar os níveis de contorno. Também definiremos o mapa de cores (colormap) para uma lista de cores e definiremos o parâmetro `extend` como `'both'` para mostrar valores fora da faixa de níveis.

```python
# Create filled contour with explicit levels
fig, ax = plt.subplots()
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
CS = ax.contourf(X, Y, Z, levels, colors=('r', 'g', 'b'),
                 origin=origin, extend='both')
CS2 = ax.contour(X, Y, Z, levels, colors=('k',),
                 linewidths=(3,), origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Explicit Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')

# Show plot
plt.show()
```
