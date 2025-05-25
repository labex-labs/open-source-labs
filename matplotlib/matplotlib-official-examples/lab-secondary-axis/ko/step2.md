# 데이터 플롯

보조 축의 사용법을 시연하기 위해 간단한 사인파를 생성합니다. x 축으로 도 (degrees) 를 사용하여 사인파를 플롯합니다.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 360, 1)
y = np.sin(2 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('angle [degrees]')
ax.set_ylabel('signal')
ax.set_title('Sine wave')
```
