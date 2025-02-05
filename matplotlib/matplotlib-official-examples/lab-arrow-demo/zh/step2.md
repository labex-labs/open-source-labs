# 定义数据并绘制箭头图

第二步是定义数据，并使用 `make_arrow_graph()` 函数绘制箭头图。我们将数据定义为一个字典，其中包含碱基和配对转换的概率。我们还将把图形的大小设置为4，并对数据进行归一化处理。

```python
# 定义数据
data = {
    'A': 0.4, 'T': 0.3, 'G': 0.6, 'C': 0.2,
    'AT': 0.4, 'AC': 0.3, 'AG': 0.2,
    'TA': 0.2, 'TC': 0.3, 'TG': 0.4,
    'CT': 0.2, 'CG': 0.3, 'CA': 0.2,
    'GA': 0.1, 'GT': 0.4, 'GC': 0.1,
}

# 绘制箭头图
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size)

plt.show()
```
