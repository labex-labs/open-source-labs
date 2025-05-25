# Criar uma seta rotacionada

Nesta etapa, criaremos uma seta direcional ancorada rotacionada. Esta seta será rotacionada em 30 graus e terá uma fonte serifada.

```python
fontprops = fm.FontProperties(family='serif')

rotated_arrow = AnchoredDirectionArrows(
                    ax.transAxes,
                    '30', '120',
                    loc='center',
                    color='w',
                    angle=30,
                    fontproperties=fontprops
                    )
ax.add_artist(rotated_arrow)
```
