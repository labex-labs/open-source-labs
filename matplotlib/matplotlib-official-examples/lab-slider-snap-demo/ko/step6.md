# 업데이트 함수 생성

이 단계에서는 슬라이더에 대한 업데이트 함수를 생성합니다. 이 함수는 슬라이더 값이 변경될 때 플롯을 업데이트합니다.

```python
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
```
