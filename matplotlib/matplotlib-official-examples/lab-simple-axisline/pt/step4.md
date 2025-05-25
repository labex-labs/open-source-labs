# Tornar a Linha do Eixo X Visível em Y=0

Agora, tornaremos a linha do eixo x visível em y=0. Isso é feito definindo o eixo xzero como visível.

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Axis Zero")
```
