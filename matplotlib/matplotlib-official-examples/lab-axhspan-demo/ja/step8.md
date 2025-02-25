# 四角形の追加

`axhspan()` と `axvspan()` 関数を使用して四角形を追加します。

```python
# y = 0.25 から y = 0.75 までの軸の幅にわたる 50% グレーの四角形。
ax.axhspan(0.25, 0.75, facecolor='0.5')
# x = 1.25 から x = 1.55 までの軸の高さにわたる緑の四角形。
ax.axvspan(1.25, 1.55, facecolor='#2ca02c')
```
