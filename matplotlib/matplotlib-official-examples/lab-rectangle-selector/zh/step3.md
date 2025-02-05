# 定义切换选择器函数

每当用户按下“t”键时，切换选择器函数都会被调用。此函数将切换RectangleSelector和EllipseSelector小部件的活动状态。

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
