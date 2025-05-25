# 메뉴 항목 설정

선택한 색상 필터 이름에 따라 메뉴 항목을 설정하는 함수를 정의합니다. 이 함수는 선택 사항에 따라 색상 필터 함수를 업데이트합니다.

```python
def _set_menu_entry(tb, name):
    tb.canvas.figure.set_agg_filter(_get_color_filter(name))
    tb.canvas.draw_idle()
```
