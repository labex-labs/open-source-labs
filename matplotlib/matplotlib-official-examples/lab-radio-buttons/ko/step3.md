# 플롯 및 라디오 버튼 생성

이제 플롯과 라디오 버튼을 생성합니다. `subplots()` 함수를 사용하여 플롯을 생성하고, `RadioButtons()` 함수를 사용하여 라디오 버튼을 생성합니다.

```python
fig, ax = plt.subplots()
l, = ax.plot(t, s0, lw=2, color='red')
fig.subplots_adjust(left=0.3)

axcolor = 'lightgoldenrodyellow'
rax = fig.add_axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('1 Hz', '2 Hz', '4 Hz'),
                     label_props={'color': 'cmy', 'fontsize': [12, 14, 16]},
                     radio_props={'s': [16, 32, 64]})
```
