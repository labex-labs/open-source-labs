# Hinzufügen von Winkelannotationspfeilen und -texten

Wir werden Winkelannotationspfeile und -texte zu jedem Klammerpfeilstil hinzufügen. Zunächst werden wir die oberen Koordinaten für die gezeichneten Patches bei _angleA_ und _angleB_ ermitteln. Dann werden wir die Verbindungsrichtungen für die Annotationspfeile definieren. Schließlich werden wir Pfeile und Annotationstexte zum Diagramm hinzufügen.

```python
    # Get the top coordinates for the drawn patches at A and B
    patch_tops = [get_point_of_rotated_vertical(center, 0.5, angle)
                  for center, angle in zip(arrow_centers, anglesAB)]
    # Define the connection directions for the annotation arrows
    connection_dirs = (1, -1) if angle > 0 else (-1, 1)
    # Add arrows and annotation text
    arrowstyle = "Simple, tail_width=0.5, head_width=4, head_length=8"
    for vline, dir, patch_top, angle in zip(vlines, connection_dirs,
                                            patch_tops, anglesAB):
        kw = dict(connectionstyle=f"arc3,rad={dir * 0.5}",
                  arrowstyle=arrowstyle, color="C0")
        ax.add_patch(FancyArrowPatch(vline, patch_top, **kw))
        ax.text(vline[0] - dir * 0.15, y + 0.7, f'{angle}°', ha="center",
                va="center")
```
