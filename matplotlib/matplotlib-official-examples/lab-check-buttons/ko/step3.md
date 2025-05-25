# 플롯 생성

이제 `matplotlib`를 사용하여 플롯을 생성합니다. 세 개의 사인파를 동일한 그래프에 플롯하고 첫 번째 파의 가시성을 `False`로 설정합니다. 이는 처음에는 숨겨진 상태로 시작하려는 의도입니다.

```python
fig, ax = plt.subplots()
l0, = ax.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
l1, = ax.plot(t, s1, lw=2, color='red', label='2 Hz')
l2, = ax.plot(t, s2, lw=2, color='green', label='3 Hz')
fig.subplots_adjust(left=0.2)
```
