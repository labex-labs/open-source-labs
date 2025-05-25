# 두 방향으로 서브플롯 쌓기

서브플롯 그리드를 생성하려면, `subplots()` 함수에 행과 열의 수를 인자로 전달할 수 있습니다. 반환된 `axs` 객체는 2 차원 NumPy 배열입니다.

```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 1].plot(x, -y, 'tab:red')
```
