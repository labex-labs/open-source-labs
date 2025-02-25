# プロットを作成する

対数カラースケール付きの塗りつぶし等高線プロットを作成するために`contourf`関数を使います。

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

cbar = fig.colorbar(cs)

plt.show()
```
