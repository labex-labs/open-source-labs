# Définissez la fonction de basculement du sélecteur

La fonction de basculement du sélecteur sera appelée chaque fois que l'utilisateur appuie sur la touche 't'. Cette fonction basculera l'état actif des widgets RectangleSelector et EllipseSelector.

```python
def toggle_selector(event):
    print('Key pressed.')
    if event.key == 't':
        for selector in selectors:
            name = type(selector).__name__
            if selector.active:
                print(f'{name} désactivé.')
                selector.set_active(False)
            else:
                print(f'{name} activé.')
                selector.set_active(True)
```
