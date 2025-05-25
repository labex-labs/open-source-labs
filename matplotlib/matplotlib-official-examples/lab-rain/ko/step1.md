# 새로운 Figure 와 Axes 생성

첫 번째 단계는 새로운 figure 와 이를 채우는 axes 를 생성하는 것입니다. 이것이 시뮬레이션이 그려질 캔버스가 됩니다.

```python
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
```
