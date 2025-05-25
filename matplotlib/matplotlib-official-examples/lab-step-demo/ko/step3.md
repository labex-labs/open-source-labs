# `.step()`을 사용하여 플롯

`.step()` 함수를 사용하여 구간별 상수 곡선을 생성할 수 있습니다. `where` 매개변수는 단계가 어디에 그려져야 하는지를 결정합니다. `where`에 대해 서로 다른 값을 사용하여 세 개의 플롯을 생성합니다.

```python
plt.step(x, y + 2, label='pre (default)', where='pre')
plt.step(x, y + 1, label='mid', where='mid')
plt.step(x, y, label='post', where='post')
plt.legend()
plt.show()
```

위 코드는 `where`에 대해 서로 다른 값을 갖는 세 개의 구간별 상수 곡선이 있는 플롯을 생성합니다.
