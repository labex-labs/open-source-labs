# グラフを作成する

このステップでは、グラフを作成します。グラフにテキストを追加するために `fig.text()` メソッドを使用します。`zip()` 関数を使ってフォントと対応するテキストのリストを反復処理し、それらをマッチングさせます。usetex モードを有効にするために `usetex` パラメータを `True` に設定します。

```python
fig = plt.figure()
for y, font, text in zip(
    range(5),
    ['ptmr8r', 'ptmri8r', 'ptmro8r', 'ptmr8rn', 'ptmrr8re'],
    [f'Nimbus Roman No9 L {x}'
     for x in ['', 'Italics (real italics for comparison)',
               '(slanted)', '(condensed)', '(extended)']],
):
    fig.text(.1, 1 - (y + 1) / 6, setfont(font) + text, usetex=True)

fig.suptitle('Usetex font effects')
plt.show()
```
