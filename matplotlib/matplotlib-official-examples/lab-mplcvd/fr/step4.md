# Configurez la barre d'outils

Ensuite, nous définissons une fonction qui configure la barre d'outils en fonction du type de backend utilisé. Cette fonction crée un bouton qui permet à l'utilisateur de sélectionner le type de filtre de couleur à simuler.

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
        raise NotImplementedError("Le backend actuel n'est pas pris en charge")
```
