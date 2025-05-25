# `.plot()`을 사용하여 플롯

`.plot()` 함수의 `drawstyle` 매개변수를 사용하여 `.step()`과 동일한 동작을 수행할 수 있습니다. `drawstyle`에 대해 서로 다른 값을 사용하여 세 개의 플롯을 생성합니다.

```python
plt.plot(x, y + 2, drawstyle='steps', label='steps (=steps-pre)')
plt.plot(x, y + 1, drawstyle='steps-mid', label='steps-mid')
plt.plot(x, y, drawstyle='steps-post', label='steps-post')
plt.legend()
plt.show()
```

위 코드는 `drawstyle`에 대해 서로 다른 값을 갖는 세 개의 구간별 상수 곡선이 있는 플롯을 생성합니다.
