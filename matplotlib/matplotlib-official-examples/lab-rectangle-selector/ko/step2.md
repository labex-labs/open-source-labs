# 선택 콜백 함수 정의

선택 콜백 함수는 사용자가 사각형 또는 타원을 선택할 때마다 호출됩니다. 이 함수는 클릭 및 릴리스 이벤트를 인수로 받아서 사각형 또는 타원의 좌표를 출력합니다.

```python
def select_callback(eclick, erelease):
    """
    Callback for line selection.

    *eclick* and *erelease* are the press and release events.
    """
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print(f"({x1:3.2f}, {y1:3.2f}) --> ({x2:3.2f}, {y2:3.2f})")
    print(f"The buttons you used were: {eclick.button} {erelease.button}")
```
