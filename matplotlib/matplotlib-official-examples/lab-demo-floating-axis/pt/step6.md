# Definir os Limites e Exibir a Grade (Grid)

Nesta etapa, definiremos os limites para os eixos e exibiremos a grade. Usaremos `set_aspect()` para definir a proporção (aspect ratio) dos eixos e `grid()` para exibir a grade.

```python
# Set the limits and display the grid
ax1.set_aspect(1.)
ax1.set_xlim(-5, 12)
ax1.set_ylim(-5, 10)
ax1.grid(True)
```
