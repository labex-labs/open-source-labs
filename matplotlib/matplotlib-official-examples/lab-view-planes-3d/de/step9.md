# Fügen einer Bezeichnung zum Mittelpunktssubplot hinzu

Wir fügen einer Bezeichnung zum Mittelpunktssubplot hinzu, um anzuzeigen, dass dies ein Diagramm von primären 3D-Ansichtsebenen ist.

```python
label ='mplot3d primäre Sichtsebenen\n' + 'ax.view_init(elev, azim, roll)'
annotate_axes(axd['L'], label, fontsize=18)
axd['L'].set_axis_off()
```
