# Definieren der Schaltrückruffunktion

Die Schaltrückruffunktion wird jedes Mal aufgerufen, wenn der Benutzer die 't'-Taste drückt. Diese Funktion wechselt den Aktivstatus der RectangleSelector- und EllipseSelector-Widgets.

```python
def toggle_selector(event):
    print('Taste gedrückt.')
    if event.key == 't':
        for selector in selectors:
            name = type(selector).__name__
            if selector.active:
                print(f'{name} deaktiviert.')
                selector.set_active(False)
            else:
                print(f'{name} aktiviert.')
                selector.set_active(True)
```
