# Ajouter des boutons de contrôle

Nous allons maintenant ajouter les boutons de contrôle à notre graphique en utilisant la fonction `CheckButtons`. Nous allons passer les lignes tracées comme étiquettes et définir la visibilité initiale de chaque ligne. Nous allons également ajuster les propriétés des boutons de contrôle pour qu'ils correspondent aux couleurs des lignes tracées.

```python
lines_by_label = {l.get_label(): l for l in [l0, l1, l2]}
line_colors = [l.get_color() for l in lines_by_label.values()]

rax = fig.add_axes([0.05, 0.4, 0.1, 0.15])
check = CheckButtons(
    ax=rax,
    labels=lines_by_label.keys(),
    actives=[l.get_visible() for l in lines_by_label.values()],
    label_props={'color': line_colors},
    frame_props={'edgecolor': line_colors},
    check_props={'facecolor': line_colors},
)
```
