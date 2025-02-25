# ズームと角度視点を設定する

`view_init` と `set_box_aspect` メソッドを使ってズームと角度視点を設定します。X 方向の角度視点を 40 度、Y 方向の角度視点を -30 度に設定し、ズームを 0.9 に設定します。

```python
# Set zoom and angle view
ax.view_init(40, -30, 0)
ax.set_box_aspect(None, zoom=0.9)
```
