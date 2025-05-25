# Criar Subplot 2

No segundo subplot, usaremos `axisartist.axislines.AxesZero` para criar automaticamente os eixos xzero e yzero. Tornaremos as outras spines invisíveis e definiremos o eixo xzero como visível.

```python
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
ax1.axis["bottom", "top", "right"].set_visible(False)
```
