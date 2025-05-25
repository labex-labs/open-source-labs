# 이벤트와 함수 연결

이제 첫 번째 창에서 버튼 누름 (button press) 이벤트를 방금 정의한 `on_press` 함수에 연결합니다.

```python
figsrc.canvas.mpl_connect('button_press_event', on_press)
```
