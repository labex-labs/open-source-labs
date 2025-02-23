# 矢印グラフをカスタマイズする

3番目のステップは、矢印グラフをカスタマイズすることです。`display`パラメータを使って、表示する矢印のプロパティを変更できます。また、`shape`パラメータを使って矢印の形状を変更できます。それぞれ`max_arrow_width`と`arrow_sep`パラメータを使って、矢印の幅と間隔を調整できます。`alpha`パラメータを使って矢印の透明度を変更できます。また、`labelcolor`パラメータを使ってラベルの色を変更できます。

```python
# カスタマイズを加えて矢印グラフを描画する
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
