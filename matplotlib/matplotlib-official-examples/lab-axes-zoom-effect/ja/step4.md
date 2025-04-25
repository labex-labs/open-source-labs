# 軸を接続する

このステップでは、軸を接続してズーム効果を作成します。4 つの軸を持つ図を作成し、zoom_effect01 と zoom_effect02 関数を使ってそれらを接続します。

```python
axs = plt.figure().subplot_mosaic([
    ["zoom1", "zoom2"],
    ["main", "main"],
])

axs["main"].set(xlim=(0, 5))
zoom_effect01(axs["zoom1"], axs["main"], 0.2, 0.8)
axs["zoom2"].set(xlim=(2, 3))
zoom_effect02(axs["zoom2"], axs["main"])

plt.show()
```
