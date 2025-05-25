# 키 누름 이벤트 함수 정의

다음으로, 키가 눌렸을 때 호출될 함수 `on_press`를 정의합니다. 이 함수는 눌린 키에 대한 정보를 담고 있는 `event` 매개변수를 받습니다. 이 예제에서는 'x' 키가 눌렸을 때 x-label 의 가시성을 토글합니다.

```python
def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()
```
