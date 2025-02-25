# Styles de remplissage des marqueurs

La couleur de bord et la couleur de remplissage des marqueurs remplis peuvent être spécifiées séparément. De plus, le `fillstyle` peut être configuré pour être non rempli, entièrement rempli ou rempli à moitié dans diverses directions. Les styles de remplissage à moitié utilisent `markerfacecoloralt` comme couleur de remplissage secondaire. Le code suivant montre comment créer des styles de remplissage de marqueurs :

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
