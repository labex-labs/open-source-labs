# Определяем функцию переключения селектора

Функция переключения селектора будет вызываться каждый раз, когда пользователь нажимает клавишу 't'. Эта функция будет переключать активный статус виджетов RectangleSelector и EllipseSelector.

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
