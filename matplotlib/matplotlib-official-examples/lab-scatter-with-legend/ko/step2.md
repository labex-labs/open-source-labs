# 여러 그룹이 있는 산점도 생성

각 그룹을 반복하고 해당 그룹에 대한 산점도를 생성하여 여러 그룹이 있는 산점도를 만들 수 있습니다. `c`, `s`, 및 `alpha` 매개변수를 사용하여 각 그룹에 대한 마커의 색상, 크기 및 투명도를 각각 지정합니다. 또한 범례에 사용될 `label` 매개변수를 그룹 이름으로 설정합니다.

```python
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
```
