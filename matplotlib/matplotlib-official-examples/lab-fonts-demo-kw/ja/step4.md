# フォントバリアントを表示する

次に、Matplotlib に用意されている異なるフォントバリアントを表示します。`fig.text()` メソッドを使って、各フォントバリアントを表示します。バリアント名をテキストとし、対応するフォントバリアントをキーワード引数とします。

```python
fig.text(0.5, 0.9, 'variant', **alignment)
variants = ['normal','small-caps']
for k, variant in enumerate(variants):
    fig.text(0.5, yp[k], variant, family='serif', variant=variant, **alignment)
```
