# Afficher les propriétés supplémentaires de la police

Dans cette étape, nous allons afficher les propriétés supplémentaires de la police qui ne sont disponibles que si la face est scalable.

```python
if font.scalable:
    # la boîte englobante globale de la face (xmin, ymin, xmax, ymax)
    print('Bbox:               ', font.bbox)
    # nombre d'unités de police couvertes par l'EM
    print('EM:                 ', font.units_per_EM)
    # l'ascenseur en 26,6 unités
    print('Ascender:           ', font.ascender)
    # le descendueur en 26,6 unités
    print('Descender:          ', font.descender)
    # la hauteur en 26,6 unités
    print('Height:             ', font.height)
    # avance horizontale maximale du curseur
    print('Max adv width:      ', font.max_advance_width)
    # pareil pour la mise en page verticale
    print('Max adv height:     ', font.max_advance_height)
    # position verticale de la barre de soulignement
    print('Underline pos:      ', font.underline_position)
    # épaisseur verticale du soulignement
    print('Underline thickness:', font.underline_thickness)
```
