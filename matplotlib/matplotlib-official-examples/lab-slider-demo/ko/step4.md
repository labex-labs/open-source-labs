# 슬라이더 생성

이제 사인파의 주파수와 진폭을 조정할 수 있는 슬라이더를 생성합니다. 주파수를 제어하기 위한 수평 슬라이더와 진폭을 제어하기 위한 수직 슬라이더를 생성합니다.

```python
fig.subplots_adjust(left=0.25, bottom=0.25)
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Frequency [Hz]',
    valmin=0.1,
    valmax=30,
    valinit=init_frequency,
)

axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Amplitude",
    valmin=0,
    valmax=10,
    valinit=init_amplitude,
    orientation="vertical"
)
```
