# 積み上げ棒グラフを作成する

`matplotlib.pyplot.bar` を使って積み上げ棒グラフを作成し、各体重カテゴリをループして棒を積み上げます。

```python
fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")
```
