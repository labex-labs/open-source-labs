# 플롯 생성

`contourf` 함수를 사용하여 로그 색상 척도를 가진 채워진 등고선 플롯을 생성합니다.

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

cbar = fig.colorbar(cs)

plt.show()
```
