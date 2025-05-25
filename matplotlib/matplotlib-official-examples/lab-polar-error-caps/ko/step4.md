# 오차 막대 생성

이 단계에서는 극 좌표축 (polar axis) 에 오차 막대를 생성합니다. `errorbar()` 함수를 사용하여 반경 (radius) 및 세타 (theta) 오차 막대를 모두 생성합니다.

```python
ax.errorbar(theta, r, xerr=0.25, yerr=0.1, capsize=7, fmt="o", c="seagreen")
```
