# 오프셋을 사용하여 RegularPolyCollection 생성

```python
col = collections.RegularPolyCollection(
    7, sizes=np.abs(xx) * 10.0, offsets=xyo, offset_transform=ax3.transData)
trans = transforms.Affine2D().scale(fig.dpi / 72.0)
col.set_transform(trans)
col.set_color(colors)

ax3.add_collection(col, autolim=True)
ax3.autoscale_view()

ax3.set_title('RegularPolyCollection using offsets')
```

여섯 번째 단계는 오프셋을 사용하여 RegularPolyCollection 을 생성하는 것입니다. RegularPolyCollection 을 사용하여 오프셋이 있는 정다각형을 생성합니다. 또한 offset_transform 을 사용하여 다각형의 위치를 설정합니다.
