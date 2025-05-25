# Construir o Gráfico de Dispersão (Scatter Plot)

Agora, construiremos o gráfico de dispersão (scatter plot), que atualizaremos durante a animação à medida que as gotas de chuva se desenvolvem.

```python
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')
```
