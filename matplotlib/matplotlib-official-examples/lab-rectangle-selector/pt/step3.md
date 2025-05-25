# Definir a função de alternância do seletor

A função de alternância do seletor será chamada toda vez que o usuário pressionar a tecla 't'. Esta função irá alternar o status ativo dos widgets `RectangleSelector` e `EllipseSelector`.

```python
def toggle_selector(event):
    print('Key pressed.')
    if event.key == 't':
        for selector in selectors:
            name = type(selector).__name__
            if selector.active:
                print(f'{name} deactivated.')
                selector.set_active(False)
            else:
                print(f'{name} activated.')
                selector.set_active(True)
```
