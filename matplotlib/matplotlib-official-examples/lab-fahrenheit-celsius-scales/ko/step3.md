# 두 번째 축을 업데이트하는 함수 정의

첫 번째 축에 따라 두 번째 축을 업데이트하기 위해 클로저 함수를 콜백 (callback) 으로 등록하여 정의합니다.

```python
def convert_ax_c_to_celsius(ax_f):
    """
    첫 번째 축에 따라 두 번째 축을 업데이트합니다.
    """
    y1, y2 = ax_f.get_ylim()
    ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
    ax_c.figure.canvas.draw()
```
