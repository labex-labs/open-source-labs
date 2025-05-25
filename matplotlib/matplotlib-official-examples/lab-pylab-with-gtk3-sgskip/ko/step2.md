# Figure 및 Axis 생성

다음으로, `subplots()` 메서드를 사용하여 figure 와 axis 를 생성합니다. 그런 다음 axis 에 두 개의 선을 그리고, 이를 구별하기 위해 범례 (legend) 를 추가합니다.

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```
