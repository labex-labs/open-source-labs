# 샘플 y=x 그래프에서 "symlog"와 "asinh" 동작 비교

샘플 y=x 그래프에서 "symlog"와 "asinh"의 동작을 비교해 보겠습니다. 동일한 그래프를 두 번 플롯할 것이며, 한 번은 "symlog"로, 다른 한 번은 "asinh"로 플롯합니다.

```python
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex=True)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')
```
