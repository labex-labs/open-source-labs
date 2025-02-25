# グラフを作成して代替カーソルを設定する

次に、グラフを作成し、ループを使って各サブプロットに代替カーソルを設定します。また、各サブプロットに使用されているカーソルを示すためのテキストも追加します。

```python
fig, axs = plt.subplots(len(Cursors), figsize=(6, len(Cursors) + 0.5), gridspec_kw={'hspace': 0})
fig.suptitle('Hover over an Axes to see alternate Cursors')

for cursor, ax in zip(Cursors, axs):
    ax.cursor_to_use = cursor
    ax.text(0.5, 0.5, cursor.name,
            horizontalalignment='center', verticalalignment='center')
    ax.set(xticks=[], yticks=[])
```
