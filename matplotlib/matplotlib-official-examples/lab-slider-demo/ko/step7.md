# 리셋 버튼 생성

이제 슬라이더를 초기 값으로 리셋하는 리셋 버튼을 생성합니다.

```python
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    freq_slider.reset()
    amp_slider.reset()
button.on_clicked(reset)
```
