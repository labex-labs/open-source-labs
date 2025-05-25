# Criar Subplot 1

No primeiro subplot, criaremos um novo eixo que passa por y=0 usando `axisartist.Axes`. Também tornaremos as outras spines invisíveis.

```python
ax0 = fig.add_subplot(gs[0, 0], axes_class=axisartist.Axes)
ax0.axis["y=0"] = ax0.new_floating_axis(nth_coord=0, value=0, axis_direction="bottom")
ax0.axis["y=0"].toggle(all=True)
ax0.axis["y=0"].label.set_text("y = 0")
ax0.axis["bottom", "top", "right"].set_visible(False)
```
