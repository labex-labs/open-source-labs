# パッチとツールチップの注釈を追加する

次に、パッチとツールチップの注釈をプロットに追加します。ツールチップの注釈は、`annotate` メソッドを使用して作成されます。`xy` パラメータをパッチの座標に設定し、`xytext` を `(0, 0)` に設定して、ツールチップをパッチの真上に配置します。また、`textcoords` パラメータを `'offset points'` に設定して、ツールチップをパッチに合わせて整列させます。`color` パラメータを `'w'` に設定してテキストを白に、`ha` を `'center'` に設定してテキストを水平方向に中央揃え、`fontsize` を `8` に設定してフォントサイズを設定し、`bbox` を設定してツールチップボックスのスタイルを設定します。

```python
for i, (item, label) in enumerate(zip(shapes, labels)):
    patch = ax.add_patch(item)
    annotate = ax.annotate(labels[i], xy=item.get_xy(), xytext=(0, 0),
                           textcoords='offset points', color='w', ha='center',
                           fontsize=8, bbox=dict(boxstyle='round, pad=.5',
                                                 fc=(.1,.1,.1,.92),
                                                 ec=(1., 1., 1.), lw=1,
                                                 zorder=1))

    ax.add_patch(patch)
    patch.set_gid(f'mypatch_{i:03d}')
    annotate.set_gid(f'mytooltip_{i:03d}')
```
