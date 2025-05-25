# 축 외부에서 삽입 생성

`bbox_to_anchor` 매개변수를 사용하여 축 외부로 확장되는 축 좌표에서 경계 상자를 지정하여 축 외부에서 삽입을 생성할 수 있습니다.

```python
# 축 외부에서 삽입 생성
axins = inset_axes(ax, width="100%", height="100%",
                   bbox_to_anchor=(1.05, .6, .5, .4),
                   bbox_transform=ax.transAxes, loc=2, borderpad=0)
```
