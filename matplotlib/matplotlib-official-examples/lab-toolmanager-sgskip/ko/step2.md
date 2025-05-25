# 주어진 gid 를 가진 선 표시

두 번째 단계는 `GroupHideTool`이라는 사용자 정의 도구를 생성하는 것입니다. `GroupHideTool` 클래스는 `ToolToggleBase`를 상속합니다. `GroupHideTool`의 `set_lines_visibility()` 메서드는 도구가 활성화되었는지 또는 비활성화되었는지에 따라 지정된 `gid`를 가진 플롯의 모든 선의 가시성을 True 또는 False 로 설정합니다.

```python
class GroupHideTool(ToolToggleBase):
    """Show lines with a given gid."""
    default_keymap = 'S'
    description = 'Show by gid'
    default_toggled = True

    def __init__(self, *args, gid, **kwargs):
        self.gid = gid
        super().__init__(*args, **kwargs)

    def enable(self, *args):
        self.set_lines_visibility(True)

    def disable(self, *args):
        self.set_lines_visibility(False)

    def set_lines_visibility(self, state):
        for ax in self.figure.get_axes():
            for line in ax.get_lines():
                if line.get_gid() == self.gid:
                    line.set_visible(state)
        self.figure.canvas.draw()
```
