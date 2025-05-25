# 리셋 버튼 생성

이 단계에서는 슬라이더에 대한 리셋 버튼을 생성합니다. 클릭하면 리셋 버튼이 슬라이더 값을 초기 값으로 재설정합니다.

```python
ax_reset = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(ax_reset, 'Reset', hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)
```
