# 오프셋을 사용하여 LineCollection 생성

```python
col = collections.LineCollection(
    [spiral], offsets=xyo, offset_transform=ax1.transData)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans)
col.set_color(colors)

ax1.add_collection(col, autolim=True)
ax1.autoscale_view()

ax1.set_title('LineCollection using offsets')
```

네 번째 단계는 오프셋을 사용하여 LineCollection 을 생성하는 것입니다. LineCollection 을 사용하여 오프셋이 있는 곡선을 생성합니다. 또한 offset_transform 을 사용하여 곡선의 위치를 설정합니다.
