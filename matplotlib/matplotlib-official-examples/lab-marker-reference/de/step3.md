# Marker-Füllstile

Die Randfarbe und die Füllfarbe von gefüllten Markern können separat angegeben werden. Darüber hinaus kann die `fillstyle` so konfiguriert werden, dass sie leer, vollständig gefüllt oder in verschiedenen Richtungen halb gefüllt ist. Die halb gefüllten Stile verwenden `markerfacecoloralt` als sekundäre Füllfarbe. Der folgende Code zeigt, wie man Marker-Füllstile erstellt:

```python
fig, ax = plt.subplots()
fig.suptitle('Marker fillstyle', fontsize=14)
fig.subplots_adjust(left=0.4)

filled_marker_style = dict(marker='o', linestyle=':', markersize=15,
                           color='darkgrey',
                           markerfacecolor='tab:blue',
                           markerfacecoloralt='lightsteelblue',
                           markeredgecolor='brown')

for y, fill_style in enumerate(Line2D.fillStyles):
    ax.text(-0.5, y, repr(fill_style), **text_style)
    ax.plot([y] * 3, fillstyle=fill_style, **filled_marker_style)
format_axes(ax)
```
