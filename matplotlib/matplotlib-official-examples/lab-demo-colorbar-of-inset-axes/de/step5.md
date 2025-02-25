# Eine Farbskala hinzufügen

Füge eine Farbskala zum eingebetteten Achsenbereich hinzu, indem du die `inset_axes`-Funktion verwendest. Setze die Breite, Höhe, den Ort und die Begrenzung der Farbskala.

```python
cax = inset_axes(axins,
                 width="5%",  # Breite = 10% der Breite der übergeordneten Bounding Box
                 height="100%",  # Höhe : 50%
                 loc='untere linke Ecke',
                 bbox_to_anchor=(1.05, 0., 1, 1),
                 bbox_transform=axins.transAxes,
                 borderpad=0,
                 )
fig.colorbar(im, cax=cax)
```
