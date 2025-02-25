# Fügen Sie eine Farbskala mit Einfügebereichen hinzu

Jetzt werden wir jeder der Bilder eine Farbskala mit Hilfe von Einfügebereichen hinzufügen. Die erste Farbskala wird zu ax1 und die zweite zu ax2 hinzugefügt.

```python
# fügen Sie der ax1 eine Farbskala hinzu
axins1 = inset_axes(
    ax1,
    width="50%",  # Breite: 50% der Breite des übergeordneten Bounding Boxes
    height="5%",  # Höhe: 5%
    loc="upper right",
)
axins1.xaxis.set_ticks_position("bottom")
fig.colorbar(im1, cax=axins1, orientation="horizontal", ticks=[1, 2, 3])

# fügen Sie der ax2 eine Farbskala hinzu
axins2 = inset_axes(
    ax2,
    width="5%",  # Breite: 5% der Breite des übergeordneten Bounding Boxes
    height="50%",  # Höhe: 50%
    loc="lower left",
    bbox_to_anchor=(1.05, 0., 1, 1),
    bbox_transform=ax2.transAxes,
    borderpad=0,
)
fig.colorbar(im2, cax=axins2, ticks=[1, 2, 3])
```
