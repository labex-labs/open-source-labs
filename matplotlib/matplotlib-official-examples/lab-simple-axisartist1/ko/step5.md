# 데이터 플롯

이제 subplot 을 생성했으므로 `np.sin(x)`를 사용하여 데이터를 플롯할 수 있습니다.

```python
x = np.arange(0, 2*np.pi, 0.01)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.sin(x))
```
