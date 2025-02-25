# Werkzeugleiste einrichten

Als nächstes definieren wir eine Funktion, die die Werkzeugleiste basierend auf dem verwendeten Backendtyp einrichtet. Diese Funktion erstellt einen Button, der dem Benutzer ermöglicht, den Typ des Farbfilters auszuwählen, den er simulieren möchte.

```python
def setup(figure):
    tb = figure.canvas.toolbar
    if tb is None:
        return
    for cls in type(tb).__mro__:
        pkg = cls.__module__.split(".")[0]
        if pkg!= "matplotlib":
            break
    if pkg == "gi":
        _setup_gtk(tb)
    elif pkg in ("PyQt5", "PySide2", "PyQt6", "PySide6"):
        _setup_qt(tb)
    elif pkg == "tkinter":
        _setup_tk(tb)
    elif pkg == "wx":
        _setup_wx(tb)
    else:
        raise NotImplementedError("The current backend is not supported")
```
