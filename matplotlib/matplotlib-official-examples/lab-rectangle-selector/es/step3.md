# Definir la función de selector de conmutación

La función de selector de conmutación se llamará cada vez que el usuario presione la tecla 't'. Esta función conmutará el estado activo de los widgets RectangleSelector y EllipseSelector.

```python
def toggle_selector(event):
    print('Key pressed.')
    if event.key == 't':
        for selector in selectors:
            name = type(selector).__name__
            if selector.active:
                print(f'{name} desactivado.')
                selector.set_active(False)
            else:
                print(f'{name} activado.')
                selector.set_active(True)
```
