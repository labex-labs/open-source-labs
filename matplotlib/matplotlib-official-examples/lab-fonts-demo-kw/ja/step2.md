# フォントファミリーを表示する

次に、Matplotlib に用意されている異なるフォントファミリーを表示します。`fig.text()` メソッドを使って、各フォントファミリーを表示します。フォントファミリー名をテキストとし、対応するフォントファミリーをキーワード引数とします。

```python
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

fig.text(0.1, 0.9, 'family', size='large', **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    fig.text(0.1, yp[k], family, family=family, **alignment)
```
