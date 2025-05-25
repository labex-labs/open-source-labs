# Deslocar os Spines

Moveremos os spines esquerdo e inferior para fora em 10 pontos usando a função `set_position()`. O argumento para `set_position()` é uma tupla com dois elementos. O primeiro elemento representa a posição do spine, e o segundo elemento representa a distância do spine para a área do gráfico.

```python
ax.spines[['left', 'bottom']].set_position(('outward', 10))
```
