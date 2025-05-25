# 기본 플롯 생성

기본 플롯을 생성하려면 x 및 y 값을 정의한 다음 `plt.plot()`을 사용하여 플롯해야 합니다. 여기서는 두 개의 사인파를 플롯합니다.

```python
x = np.arange(0.0, 2.0, 0.02)
y1 = np.sin(2 * np.pi * x)
y2 = np.sin(4 * np.pi * x)

plt.plot(x, y1, label='sin(2pix)')
plt.plot(x, y2, label='sin(4pix)')
```
