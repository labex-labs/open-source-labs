# 그래프 플롯

이제 예제 데이터가 있으므로 `errorbar()` 함수를 사용하여 그래프를 플롯할 수 있습니다. `x` 및 `y` 배열을 처음 두 매개변수로 전달합니다. 그런 다음 `xerr` 및 `yerr` 매개변수를 사용하여 x 방향의 오차를 0.2 로, y 방향의 오차를 0.4 로 지정합니다.

```python
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.show()
```
