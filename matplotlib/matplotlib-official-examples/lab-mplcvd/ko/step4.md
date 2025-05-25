# 툴바 설정

다음으로, 사용된 백엔드 (backend) 유형에 따라 툴바를 설정하는 함수를 정의합니다. 이 함수는 사용자가 시뮬레이션할 색상 필터 유형을 선택할 수 있는 버튼을 생성합니다.

```python
def setup(figure):
    tb = figure.canvas.toolbar
    if tb is None:
        return
    for cls in type(tb).__mro__:
        pkg = cls.__module__.split(".")[0]
        if pkg != "matplotlib":
            break
    if pkg == "gi":
        _setup_gtk(tb)
    elif pkg in ("PyQt5", "PySide2", "PyQt6", "PySide6"):
        _setup_qt(tb)
    elif pkg == "tkinter":
        _setup_tk(tb)
    elif pkg == "wx":
        _setup_wx(tb)
    else:
        raise NotImplementedError("The current backend is not supported")
```
