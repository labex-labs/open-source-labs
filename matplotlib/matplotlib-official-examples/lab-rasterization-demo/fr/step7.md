# Créer un tracé pcolormesh avec un texte superposé avec rastérisation

Nous allons créer un tracé pcolormesh avec un texte superposé avec rastérisation pour illustrer la manière dont la rastérisation peut permettre aux graphiques vectoriels de conserver les avantages des graphiques vectoriels pour certains artistes tels que les axes et le texte.

```python
ax4.set_aspect(1)
m = ax4.pcolormesh(xx, yy, d, zorder=-10)
ax4.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax4.transAxes)
ax4.set_rasterization_zorder(0)
ax4.set_title("Rasterization z$<-10$")
```
