# 極座標軸上に散布図を作成する

`plt.scatter()` 関数を使って極座標軸上に散布図を作成します。`projection` パラメータを `'polar'` に設定し、半径、角度、色、面積の値をパラメータとして渡します。

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
```
