# Desenhar uma seta entre diferentes eixos

Vamos desenhar uma seta entre o mesmo ponto em coordenadas de dados, mas em diferentes eixos.

```python
xy = (0.3, 0.2)
con = ConnectionPatch(
    xyA=xy, coordsA=ax2.transData,
    xyB=xy, coordsB=ax1.transData,
    arrowstyle="->", shrinkB=5)
fig.add_artist(con)
```
