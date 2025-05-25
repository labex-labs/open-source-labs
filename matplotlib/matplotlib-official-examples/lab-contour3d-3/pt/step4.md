# Projetar perfis de contorno nas paredes do gráfico

Nesta etapa, projetaremos perfis de contorno nas paredes do gráfico, plotando os contornos para cada dimensão com deslocamentos apropriados.

```python
# Plotar projeções dos contornos para cada dimensão
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
