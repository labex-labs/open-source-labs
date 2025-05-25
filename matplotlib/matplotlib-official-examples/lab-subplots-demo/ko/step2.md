# 한 방향으로 서브플롯 쌓기

수직 또는 수평으로 쌓인 여러 서브플롯을 생성하려면, `subplots()` 함수에 행과 열의 수를 인자로 전달할 수 있습니다. 반환된 `axs` 객체는 생성된 `Axes` 목록을 포함하는 1 차원 numpy 배열입니다.

```python
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].plot(x, -y)
```
