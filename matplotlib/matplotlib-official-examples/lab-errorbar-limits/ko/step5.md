# 하한 추가

오차 막대에 하한을 추가하려면 `errorbar` 함수의 `lolims` 매개변수를 사용합니다. 또한 이전 플롯들과 구별하기 위해 y 값에 1.0 의 상수 값을 추가합니다.

```python
# including lower limits
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=True, linestyle='dotted')
```
