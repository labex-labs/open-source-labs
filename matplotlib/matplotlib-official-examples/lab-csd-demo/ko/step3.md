# 신호 플롯

Matplotlib 의 plot 함수를 사용하여 생성된 두 신호를 플롯할 수 있습니다.

```python
fig, ax = plt.subplots()
ax.plot(t, s1, label='s1')
ax.plot(t, s2, label='s2')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.legend()
plt.show()
```
