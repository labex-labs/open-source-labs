# Define the toggle selector function

The toggle selector function will be called every time the user presses the 't' key. This function will toggle the active status of the RectangleSelector and EllipseSelector widgets.

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
