# 사용자 정의 figure 서브클래스 생성

플롯에 텍스트 워터마크를 추가하는 `WatermarkFigure`라는 사용자 정의 figure 서브클래스를 생성합니다. 이 클래스는 Matplotlib 의 `Figure` 클래스를 상속합니다.

```python
from matplotlib.figure import Figure

class WatermarkFigure(Figure):
    """A figure with a text watermark."""

    def __init__(self, *args, watermark=None, **kwargs):
        super().__init__(*args, **kwargs)

        if watermark is not None:
            bbox = dict(boxstyle='square', lw=3, ec='gray',
                        fc=(0.9, 0.9, .9, .5), alpha=0.5)
            self.text(0.5, 0.5, watermark,
                      ha='center', va='center', rotation=30,
                      fontsize=40, color='gray', alpha=0.5, bbox=bbox)
```
