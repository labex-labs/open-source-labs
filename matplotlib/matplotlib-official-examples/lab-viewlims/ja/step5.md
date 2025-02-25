# ズーム機能を追加する

xlim_changed と ylim_changed イベントを UpdatingRect と MandelbrotDisplay オブジェクトに接続することで、ズーム機能を追加します。

```python
ax2.callbacks.connect('xlim_changed', rect)
ax2.callbacks.connect('ylim_changed', rect)

ax2.callbacks.connect('xlim_changed', md.ax_update)
ax2.callbacks.connect('ylim_changed', md.ax_update)
ax2.set_title("Zoom here")
```
