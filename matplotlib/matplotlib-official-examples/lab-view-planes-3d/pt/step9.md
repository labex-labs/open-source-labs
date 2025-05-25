# Adicionar um rótulo ao subplot central

Adicionamos um rótulo ao subplot central para indicar que este é um gráfico de planos de visualização 3D primários.

```python
label = 'mplot3d primary view planes\n' + 'ax.view_init(elev, azim, roll)'
annotate_axes(axd['L'], label, fontsize=18)
axd['L'].set_axis_off()
```
