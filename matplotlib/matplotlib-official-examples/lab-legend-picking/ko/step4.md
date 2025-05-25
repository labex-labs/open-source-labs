# 선 및 범례 생성

Matplotlib 을 사용하여 두 개의 선과 범례를 생성합니다.

```python
line1, = ax.plot(t, y1, lw=2, label='1 Hz')
line2, = ax.plot(t, y2, lw=2, label='2 Hz')
leg = ax.legend(fancybox=True, shadow=True)
```
