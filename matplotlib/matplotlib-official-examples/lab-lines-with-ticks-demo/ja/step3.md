# Ticked Patheffect を使って曲線を描画する

ここでは、Ticked Patheffect を使って曲線を描画します。

```python
# Plot a curved line with ticked style path
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```
