# Créez la classe AnnotatedCursor

Nous créons une nouvelle classe `AnnotatedCursor` qui hérite de `matplotlib.widgets.Cursor` et qui démontre la création de nouveaux widgets et de leurs rappels d'événements. La classe `AnnotatedCursor` est utilisée pour créer un curseur en croix avec un texte montrant les coordonnées actuelles.

```python
class AnnotatedCursor(Cursor):
    """
    Un curseur en croix comme `~matplotlib.widgets.Cursor` avec un texte montrant \
    les coordonnées actuelles.
  ...
    """
```
