# 클래스로 사용자 정의 박스 스타일 구현하기

사용자 정의 박스 스타일은 `__call__`을 구현하는 클래스로도 구현할 수 있습니다. 그런 다음 클래스를 `BoxStyle._style_list` 딕셔너리에 등록할 수 있으며, 이를 통해 문자열로 박스 스타일을 지정할 수 있습니다. `bbox=dict(boxstyle="registered_name,param=value,...", ...)`.

```python
class MyStyle:
    """A simple box."""

    def __init__(self, pad=0.3):
        """
        인수는 float 여야 하며 기본값을 가져야 합니다.

        Parameters
        ----------
        pad : float
            패딩 양
        """
        self.pad = pad
        super().__init__()

    def __call__(self, x0, y0, width, height, mutation_size):
        """
        박스의 위치와 크기가 주어지면, 그 주변의 박스 경로를 반환합니다.

        회전은 자동으로 처리됩니다.

        Parameters
        ----------
        x0, y0, width, height : float
            박스 위치 및 크기.
        mutation_size : float
            변형에 대한 참조 스케일, 일반적으로 텍스트 글꼴 크기.
        """
        # 패딩
        pad = mutation_size * self.pad
        # 패딩이 추가된 너비와 높이
        width = width + 2.*pad
        height = height + 2.*pad
        # 패딩된 박스의 경계
        x0, y0 = x0 - pad, y0 - pad
        x1, y1 = x0 + width, y0 + height
        # 새로운 경로 반환
        return Path([(x0, y0),
                     (x1, y0), (x1, y1), (x0, y1),
                     (x0-pad, (y0+y1)/2.), (x0, y0),
                     (x0, y0)],
                    closed=True)


BoxStyle._style_list["angled"] = MyStyle  # 사용자 정의 스타일 등록.

fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))

del BoxStyle._style_list["angled"]  # 등록 해제.

plt.show()
```
