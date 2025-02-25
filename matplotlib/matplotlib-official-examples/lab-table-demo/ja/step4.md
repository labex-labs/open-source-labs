# カラースキームを作成する

`plt.cm.BuPu`関数を使って、テーブル用のカラースキームを作成します。行には薄い青色と紫色のパステル色を使います。

```python
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
```
