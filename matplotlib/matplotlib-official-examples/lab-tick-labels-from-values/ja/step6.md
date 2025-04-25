# 目盛りフォーマッタとロケータを設定する

ステップ 5 で作成したフォーマット関数を使って、x 軸の目盛りフォーマッタを設定します。`set_major_formatter()` メソッドを使用します。また、x 軸の目盛りロケータを `MaxNLocator(integer=True)` に設定して、目盛り値が整数値をとるようにします。

```python
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
```
