# Acceder a la barra de herramientas y el contenedor vertical (vbox)

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```

Accedemos a los atributos `toolbar` y `vbox` del administrador del lienzo de la figura.
