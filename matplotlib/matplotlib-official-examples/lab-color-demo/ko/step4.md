# 차트 생성

이제 지정한 데이터와 색상을 사용하여 차트를 생성할 수 있습니다.

```python
fig, ax = plt.subplots(facecolor=(.18, .31, .31))
ax.set_facecolor('#eafff5')
ax.set_title('Voltage vs. time chart', color='0.7')
ax.set_xlabel('Time [s]', color='c')
ax.set_ylabel('Voltage [mV]', color='peachpuff')
ax.plot(t, s, 'xkcd:crimson')
ax.plot(t, .7*s, color='C4', linestyle='--')
ax.tick_params(labelcolor='tab:orange')
```
