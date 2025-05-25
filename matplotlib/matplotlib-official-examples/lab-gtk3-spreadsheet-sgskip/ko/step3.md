# 윈도우 설정

이 단계에서는 데이터를 표시할 윈도우를 설정합니다. 제목과 크기로 윈도우를 초기화하는 것으로 시작합니다.

```python
def __init__(self):
    super().__init__()
    self.set_default_size(600, 600)
    self.connect('destroy', lambda win: Gtk.main_quit())
    self.set_title('GtkListStore demo')
    self.set_border_width(8)
```
