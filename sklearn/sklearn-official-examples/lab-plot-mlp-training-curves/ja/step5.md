# 各データセットの学習曲線をプロットする

最後に、`plot_on_dataset` 関数を使用して各データセットの学習曲線をプロットできます。2x2 のグラフを作成し、各データセットを別々の軸にプロットします。

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

for ax, data, name in zip(
    axes.ravel(), data_sets, ["iris", "digits", "circles", "moons"]
):
    plot_on_dataset(*data, ax=ax, name=name)

fig.legend(ax.get_lines(), labels, ncol=3, loc="upper center")
plt.show()
```
