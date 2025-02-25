# Ticked Patheffect を使って直線を描画する

ここでは、Ticked Patheffect を使って対角線の直線を描画します。

```python
# Plot a straight diagonal line with ticked style path
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1], [0, 1], label="Line",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])
```
