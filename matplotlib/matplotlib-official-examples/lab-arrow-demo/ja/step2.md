# データを定義して矢印グラフを描画する

2番目のステップは、データを定義して、`make_arrow_graph()`関数を使って矢印グラフを描画することです。データを、塩基とペア遷移の確率を持つ辞書として定義します。また、プロットのサイズを4に設定し、データを正規化します。

```python
# データを定義する
data = {
    'A': 0.4, 'T': 0.3, 'G': 0.6, 'C': 0.2,
    'AT': 0.4, 'AC': 0.3, 'AG': 0.2,
    'TA': 0.2, 'TC': 0.3, 'TG': 0.4,
    'CT': 0.2, 'CG': 0.3, 'CA': 0.2,
    'GA': 0.1, 'GT': 0.4, 'GC': 0.1,
}

# 矢印グラフを描画する
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size)

plt.show()
```
