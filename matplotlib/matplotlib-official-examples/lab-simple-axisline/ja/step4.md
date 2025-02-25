# y = 0 のときに x 軸線を表示する

ここでは、y = 0 のときに x 軸線を表示します。これは、xzero 軸を表示可能にすることで行われます。

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Axis Zero")
```
