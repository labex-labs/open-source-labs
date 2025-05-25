# 상한 및 하한 추가

오차 막대에 상한과 하한을 모두 추가하려면 `errorbar` 함수의 `uplims` 및 `lolims` 매개변수를 모두 사용합니다. 또한 이전 플롯들과 구별하기 위해 플롯에 마커를 추가합니다.

```python
# including upper and lower limits
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr, lolims=True, uplims=True,
            marker='o', markersize=8, linestyle='dotted')
```
