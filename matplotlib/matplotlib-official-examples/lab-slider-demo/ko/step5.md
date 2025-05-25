# 업데이트 함수 생성

이제 슬라이더를 조정할 때마다 사인파를 업데이트하는 함수를 생성합니다. 이 함수는 진폭 및 주파수 슬라이더의 값을 입력받아 그에 따라 사인파를 업데이트합니다.

```python
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()
```
