# `{}` スタイルの書式指定文字列を使用した棒グラフのラベリング

このステップでは、棒グラフのラベルを書式設定するために `{}` スタイルの書式指定文字列をどのように使用するかを示します。アイスクリームの味別売上データをいくつか使います。

```python
fruit_names = ['Coffee', 'Salted Caramel', 'Pistachio']
fruit_counts = [4000, 2000, 7000]

fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor', ylim=(0, 8000))
ax.bar_label(bar_container, fmt='{:,.0f}')
```
