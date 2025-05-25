# 데이터 정의 및 화살표 그래프 플롯

두 번째 단계는 데이터를 정의하고 `make_arrow_graph()` 함수를 사용하여 화살표 그래프를 플롯하는 것입니다. 우리는 데이터를 염기 및 쌍 전이에 대한 확률을 포함하는 딕셔너리로 정의합니다. 또한 플롯의 크기를 4 로 설정하고 데이터를 정규화합니다.

```python
# Define the data
data = {
    'A': 0.4, 'T': 0.3, 'G': 0.6, 'C': 0.2,
    'AT': 0.4, 'AC': 0.3, 'AG': 0.2,
    'TA': 0.2, 'TC': 0.3, 'TG': 0.4,
    'CT': 0.2, 'CG': 0.3, 'CA': 0.2,
    'GA': 0.1, 'GT': 0.4, 'GC': 0.1,
}

# Plot the arrow graph
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size)

plt.show()
```
