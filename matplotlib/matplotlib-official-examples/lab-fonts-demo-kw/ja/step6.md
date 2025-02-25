# フォントサイズを表示する

最後に、Matplotlib に用意されている異なるフォントサイズを表示します。`fig.text()` メソッドを使って、各フォントサイズを表示します。サイズ名をテキストとし、対応するフォントサイズをキーワード引数とします。

```python
fig.text(0.9, 0.9,'size', **alignment)
sizes = [
    'xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    fig.text(0.9, yp[k], size, size=size, **alignment)
```
