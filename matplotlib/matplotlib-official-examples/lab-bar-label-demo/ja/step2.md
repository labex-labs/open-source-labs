# 垂直棒グラフのラベリング

まず、垂直棒グラフを作成して、`bar_label`関数を使ってそれにラベルを付けます。使用するデータは、性別別のペンギンの数で、https://allisonhorst.github.io/palmerpenguins/ から取得しました。

```python
species = ('Adelie', 'Chinstrap', 'Gentoo')
sex_counts = {
    'Male': np.array([73, 34, 61]),
    'Female': np.array([73, 34, 58]),
}
width = 0.6  # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()
bottom = np.zeros(3)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()
```
