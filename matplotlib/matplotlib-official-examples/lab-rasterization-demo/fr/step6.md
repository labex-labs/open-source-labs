# Créer un tracé pcolormesh avec un texte superposé sans rastérisation

Nous allons créer un tracé pcolormesh avec un texte superposé sans rastérisation pour illustrer la manière dont les graphiques vectoriels peuvent conserver les avantages des graphiques vectoriels pour certains artistes tels que les axes et le texte.

```python
ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterization")
```
