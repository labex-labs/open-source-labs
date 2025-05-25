# 화살표 그래프 사용자 정의

세 번째 단계는 화살표 그래프를 사용자 정의하는 것입니다. `display` 매개변수를 사용하여 표시할 화살표 속성을 변경할 수 있습니다. 또한 `shape` 매개변수를 사용하여 화살표의 모양을 변경할 수 있습니다. `max_arrow_width` 및 `arrow_sep` 매개변수를 사용하여 화살표의 너비와 간격을 각각 조정할 수 있습니다. `alpha` 매개변수를 사용하여 화살표의 투명도를 변경할 수 있습니다. 또한 `labelcolor` 매개변수를 사용하여 레이블의 색상을 변경할 수 있습니다.

```python
# Plot the arrow graph with customizations
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size, shape='full', max_arrow_width=0.05,
        arrow_sep=0.03, alpha=0.7, labelcolor='white')

plt.show()
```
