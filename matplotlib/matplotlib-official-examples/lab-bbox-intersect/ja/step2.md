# 矩形を設定する

矩形の位置と寸法を、`left`、`bottom`、`width`、および`height`変数を使って定義します。そして、`Rectangle`クラスを使って矩形を作成し、`add_patch`メソッドを使ってそれをグラフに追加します。

```python
left, bottom, width, height = (-1, -1, 2, 2)
rect = plt.Rectangle((left, bottom), width, height,
                     facecolor="black", alpha=0.1)

fig, ax = plt.subplots()
ax.add_patch(rect)
```
