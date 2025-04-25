# 軸のスタイルを設定する

最後に、目盛りのラベルと範囲を指定することで x 軸のスタイルを設定します。これを行うために、ヘルパー関数`set_axis_style`を定義します。

```python
# set style for the axes
labels = ['A', 'B', 'C', 'D']
set_axis_style(ax2, labels)

def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample Name')
```
