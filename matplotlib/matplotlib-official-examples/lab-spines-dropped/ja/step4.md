# スパインをオフセットする

`set_position()` 関数を使って、左と下のスパインを 10 ポイント外側に移動させます。`set_position()` の引数は、2 つの要素を持つタプルです。最初の要素はスパインの位置を表し、2 番目の要素はスパインからプロット領域までの距離を表します。

```python
ax.spines[['left', 'bottom']].set_position(('outward', 10))
```
