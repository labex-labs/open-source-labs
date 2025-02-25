# タイトルのフォントを設定する

`Axes` クラスの `set_title()` メソッドを使って、グラフのタイトルのフォントを設定します。フォントパスを `font` パラメータとして渡し、フォントファイルの名前をグラフのタイトルとして渡します。

```python
ax.set_title(f'This is a special font: {fpath.name}', font=fpath)
```
