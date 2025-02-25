# チックの方向/側

このステップでは、チックの側を変更します。

```python
fig, ax = plt.subplots(figsize=(6, 6))
line_x = line_y = [0, 1]
ax.plot(line_x, line_y, label="Line",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])

ax.plot(line_x, line_y, label="Opposite side",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=-135)])

ax.legend()
plt.show()
```

このコードは、両側にチックがある線を作成します。
