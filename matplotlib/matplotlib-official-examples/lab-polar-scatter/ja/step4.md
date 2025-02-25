# 原点をオフセットした極座標軸上に散布図を作成する

`PolarAxes` オブジェクトの `set_rorigin()` と `set_theta_zero_location()` メソッドを設定することで、原点をオフセットした極座標軸上に散布図を作成できます。原点半径を `-2.5` に設定し、オフセット `10` でゼロ位置のゼータを `'W'` に設定します。

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
```
