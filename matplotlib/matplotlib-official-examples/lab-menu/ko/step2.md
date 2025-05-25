# ItemProperties 클래스 정의

다음으로, 각 메뉴 항목의 속성을 설정하는 데 사용될 `ItemProperties` 클래스를 정의합니다. 이 클래스를 사용하여 각 항목의 글꼴 크기, 레이블 색상, 배경 색상 및 알파 값을 설정할 수 있습니다.

```python
class ItemProperties:
    def __init__(self, fontsize=14, labelcolor='black', bgcolor='yellow',
                 alpha=1.0):
        self.fontsize = fontsize
        self.labelcolor = labelcolor
        self.bgcolor = bgcolor
        self.alpha = alpha
```
