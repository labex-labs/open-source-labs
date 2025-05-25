# 토글 선택기 함수 정의

토글 선택기 함수는 사용자가 't' 키를 누를 때마다 호출됩니다. 이 함수는 RectangleSelector 및 EllipseSelector 위젯의 활성 상태를 토글합니다.

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
