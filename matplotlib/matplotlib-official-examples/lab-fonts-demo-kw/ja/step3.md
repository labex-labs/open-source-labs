# フォントスタイルを表示する

次に、Matplotlib に用意されている異なるフォントスタイルを表示します。`fig.text()` メソッドを使って、各フォントスタイルを表示します。フォントスタイル名をテキストとし、対応するフォントスタイルをキーワード引数とします。

```python
fig.text(0.3, 0.9,'style', **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    fig.text(0.3, yp[k], style, family='sans-serif', style=style, **alignment)
```
