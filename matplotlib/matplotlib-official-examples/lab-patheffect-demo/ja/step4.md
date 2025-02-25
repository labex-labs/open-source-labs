# 凡例に影のエフェクトを追加する

`withSimplePatchShadow` パスエフェクトを使用して、凡例に影のエフェクトを追加することができます。

```python
# Create plot and add shadow effect to legend
fig, ax = plt.subplots()
p1, = ax.plot([0, 1], [0, 1])
leg = ax.legend([p1], ["Line 1"], fancybox=True, loc='upper left')
leg.legendPatch.set_path_effects([patheffects.withSimplePatchShadow()])

plt.show()
```
