# 오프셋을 사용하여 PolyCollection 생성

```python
col = collections.PolyCollection(
    [spiral], offsets=xyo, offset_transform=ax2.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)
col.set_color(colors)

ax2.add_collection(col, autolim=True)
ax2.autoscale_view()

ax2.set_title('PolyCollection using offsets')
```

다섯 번째 단계는 오프셋을 사용하여 PolyCollection 을 생성하는 것입니다. PolyCollection 을 사용하여 곡선을 색상으로 채웁니다. 또한 offset_transform 을 사용하여 곡선의 위치를 설정합니다.
