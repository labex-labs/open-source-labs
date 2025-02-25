# グラフを作成する

それぞれの線スタイルのセットに対して `plot_linestyles` 関数を呼び出すことで、グラフを作成できます。

```python
fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(10, 8), height_ratios=[1, 3])

plot_linestyles(ax0, linestyle_str[::-1], title='Named linestyles')
plot_linestyles(ax1, linestyle_tuple[::-1], title='Parametrized linestyles')

plt.tight_layout()
plt.show()
```
