# Configurar a barra de ferramentas

Em seguida, definimos uma função que configura a barra de ferramentas com base no tipo de backend usado. Esta função cria um botão que permite ao usuário selecionar o tipo de filtro de cores a ser simulado.

```python
def setup(figure):
    tb = figure.canvas.toolbar
    if tb is None:
        return
    for cls in type(tb).__mro__:
        pkg = cls.__module__.split(".")[0]
        if pkg != "matplotlib":
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
        raise NotImplementedError("O backend atual não é suportado")
```
