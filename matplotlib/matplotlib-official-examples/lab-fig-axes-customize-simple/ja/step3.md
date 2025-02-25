# グラフに軸を追加する

`fig.add_axes()` メソッドを使って、グラフに軸を追加します。また、`rect.set_facecolor()` メソッドを使って、軸の背景色を設定します。

```python
ax1 = fig.add_axes([0.1, 0.3, 0.4, 0.4])
rect = ax1.patch
rect.set_facecolor('lightslategray')
```
