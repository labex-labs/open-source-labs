# 슬라이더 생성

이 단계에서는 슬라이더를 생성합니다. 진폭에 대한 슬라이더 하나와 주파수에 대한 슬라이더 하나를 생성합니다.

```python
samp = Slider(
    ax_amp, "Amp", 0.1, 9.0,
    valinit=a0, valstep=allowed_amplitudes,
    color="green"
)

sfreq = Slider(
    ax_freq, "Freq", 0, 10*np.pi,
    valinit=2*np.pi, valstep=np.pi,
    initcolor='none'  # Remove the line marking the valinit position.
)
```
