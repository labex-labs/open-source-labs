# 極座標グラフの作成

次に、グラフを定義して極座標投影を持つことを指定することで、極座標グラフを作成します。また、プロットに使用する半径とセタ値も定義します。

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
line, = ax.plot(theta, r, color='#ee8d18', lw=3)
```
