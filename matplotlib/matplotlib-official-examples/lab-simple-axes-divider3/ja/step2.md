# グラフと軸を設定する

`fig.add_axes` メソッドを使って、グラフオブジェクトを作成し、4つの軸オブジェクトを設定します。

```python
fig = plt.figure(figsize=(5.5, 4))
rect = (0.1, 0.1, 0.8, 0.8)
ax = [fig.add_axes(rect, label="%d" % i) for i in range(4)]
```
