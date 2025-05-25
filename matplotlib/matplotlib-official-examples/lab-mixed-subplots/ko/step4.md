# 2D 플롯 생성

이 단계에서는 감쇠 진동의 2D 플롯을 생성합니다.

```python
ax1 = fig.add_subplot(2, 1, 1)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
t3 = np.arange(0.0, 2.0, 0.01)

ax1.plot(t1, f(t1), 'bo',
         t2, f(t2), 'k--', markerfacecolor='green')
ax1.grid(True)
ax1.set_ylabel('Damped oscillation')
```
