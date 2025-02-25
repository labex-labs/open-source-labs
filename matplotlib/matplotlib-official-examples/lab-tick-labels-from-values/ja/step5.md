# フォーマット関数を作成する

メモリ位置の値から目盛りラベルを決定するフォーマット関数を作成します。目盛り値が `xs` の範囲内の整数の場合、`labels` リストから対応するラベルが返されます。それ以外の場合は空の文字列を返します。

```python
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''
```
