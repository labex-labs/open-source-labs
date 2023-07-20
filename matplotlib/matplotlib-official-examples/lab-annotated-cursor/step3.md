# Create the AnnotatedCursor class

We create a new class `AnnotatedCursor` that inherits from `matplotlib.widgets.Cursor` and demonstrates the creation of new widgets and their event callbacks. The `AnnotatedCursor` class is used to create a crosshair cursor with a text showing the current coordinates.

```python
class AnnotatedCursor(Cursor):
    """
    A crosshair cursor like `~matplotlib.widgets.Cursor` with a text showing \
    the current coordinates.
    ...
    """
```
