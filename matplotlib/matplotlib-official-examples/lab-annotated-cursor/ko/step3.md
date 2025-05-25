# AnnotatedCursor 클래스 생성

`matplotlib.widgets.Cursor`에서 상속받고 새로운 위젯과 해당 이벤트 콜백의 생성을 보여주는 새로운 클래스 `AnnotatedCursor`를 생성합니다. `AnnotatedCursor` 클래스는 현재 좌표를 표시하는 텍스트가 있는 십자형 커서를 생성하는 데 사용됩니다.

```python
class AnnotatedCursor(Cursor):
    """
    A crosshair cursor like `~matplotlib.widgets.Cursor` with a text showing \
    the current coordinates.
    ...
    """
```
