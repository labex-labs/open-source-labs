# x 軸の目盛りラベルを上部に移動する

x 軸の目盛りラベルを上部に移動するには、`tick_params()` 関数を使用し、`top` と `labeltop` パラメータを `True` に、`bottom` と `labelbottom` パラメータを `False` に設定します。

```python
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
```
