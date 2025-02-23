# Erstellen der AnnotatedCursor-Klasse

Wir erstellen eine neue Klasse `AnnotatedCursor`, die von `matplotlib.widgets.Cursor` erbt und die Erstellung neuer Widgets und deren Ereignisrufe demonstriert. Die `AnnotatedCursor`-Klasse wird verwendet, um einen Kreuzhaarschreiber mit einem Text zu erstellen, der die aktuellen Koordinaten anzeigt.

```python
class AnnotatedCursor(Cursor):
    """
    A crosshair cursor like `~matplotlib.widgets.Cursor` with a text showing \
    the current coordinates.
  ...
    """
```
