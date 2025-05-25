# 텍스트 상자 추가

그림의 왼쪽 상단 모서리에 서로 다른 모서리로 고정된 두 개의 텍스트 상자를 그림에 추가합니다.

```python
at = AnchoredText("Figure 1a",
                  loc='upper left', prop=dict(size=8), frameon=True,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)

at2 = AnchoredText("Figure 1(b)",
                   loc='lower left', prop=dict(size=8), frameon=True,
                   bbox_to_anchor=(0., 1.),
                   bbox_transform=ax.transAxes
                   )
at2.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at2)
```
