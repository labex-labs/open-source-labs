# round_numbers autolimit_mode 를 사용한 산점도 그리기

이 단계에서는 `axes.autolimit_mode`를 'round_numbers'로 전환하고 틱을 둥근 숫자로 유지하고 가장자리에도 틱을 표시하기 위해 산점도 (scatter plot) 를 생성합니다.

```python
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
```
