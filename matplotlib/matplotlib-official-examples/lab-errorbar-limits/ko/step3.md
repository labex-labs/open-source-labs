# 간단한 오차 막대 그래프 생성

`errorbar` 함수를 사용하여 표준 오차 막대가 있는 간단한 오차 막대 그래프를 생성합니다. 여기서는 x 및 y 값과 해당 오차 값을 설정합니다. 또한 선 스타일을 점선으로 설정합니다.

```python
fig, ax = plt.subplots(figsize=(7, 4))

# standard error bars
ax.errorbar(x, y, xerr=xerr, yerr=yerr, linestyle='dotted')
```
