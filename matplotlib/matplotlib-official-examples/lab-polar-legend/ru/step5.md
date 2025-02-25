# Настроить график

Мы можем настроить наш график, изменив цвет сетки и добавив легенду. В этом примере мы сместить легенду немного от центра графика, чтобы избежать наложения.

```python
ax.tick_params(grid_color="palegoldenrod")
angle = np.deg2rad(67.5)
ax.legend(loc="lower left",
          bbox_to_anchor=(.5 + np.cos(angle)/2,.5 + np.sin(angle)/2))
```
