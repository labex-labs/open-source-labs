# Criar uma seta simples

Agora, criaremos uma seta direcional ancorada simples usando a classe `AnchoredDirectionArrows`. Esta seta indicará as direções X e Y no gráfico.

```python
# Simple example
simple_arrow = AnchoredDirectionArrows(ax.transAxes, 'X', 'Y')
ax.add_artist(simple_arrow)
```
