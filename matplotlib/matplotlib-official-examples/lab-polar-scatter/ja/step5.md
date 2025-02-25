# セクタに制限された極座標軸上に散布図を作成する

`PolarAxes` オブジェクトの `set_thetamin()` と `set_thetamax()` メソッドを設定することで、セクタに制限された極座標軸上に散布図を作成できます。ゼータの開始と終了の制限をそれぞれ `45` と `135` に設定します。

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
```
