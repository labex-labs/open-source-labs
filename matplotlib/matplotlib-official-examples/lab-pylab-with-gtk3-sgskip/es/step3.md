# Acceder a la barra de herramientas y el VBox

Accederemos a los atributos de barra de herramientas y vbox del administrador del lienzo de la figura utilizando los métodos `manager.toolbar` y `manager.vbox`, respectivamente.

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```
