# 신호 플롯

이제 Matplotlib 을 사용하여 두 신호를 시간 도메인에서 플롯할 수 있습니다.

```python
fig, axs = plt.subplots(2, 1)
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('s1 and s2')
axs[0].grid(True)
```
