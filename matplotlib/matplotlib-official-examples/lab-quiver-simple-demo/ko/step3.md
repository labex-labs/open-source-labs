# Quiver Plot 생성

`ax.quiver()` 함수를 사용하여 quiver plot 을 생성할 수 있습니다. `X`, `Y`, `U`, 및 `V` 배열을 매개변수로 전달합니다.

```python
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
```
