# 상한 추가

오차 막대에 상한을 추가하려면 `errorbar` 함수의 `uplims` 매개변수를 사용합니다. 또한 이전 플롯과 구별하기 위해 y 값에 0.5 의 상수 값을 추가합니다.

```python
# including upper limits
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```
