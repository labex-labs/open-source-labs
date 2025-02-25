# フォントの太さを表示する

次に、Matplotlib に用意されている異なるフォントの太さを表示します。`fig.text()` メソッドを使って、各フォントの太さを表示します。太さ名をテキストとし、対応するフォントの太さをキーワード引数とします。

```python
fig.text(0.7, 0.9, 'weight', **alignment)
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    fig.text(0.7, yp[k], weight, weight=weight, **alignment)
```
