# 2-튜플 경계 상자로 삽입 생성

인치 단위로 너비와 높이를 지정하고 `bbox_to_anchor` 매개변수를 사용하여 삽입의 왼쪽 하단 모서리를 지정하여 2-튜플 경계 상자로 삽입을 생성할 수 있습니다.

```python
# 2-튜플 경계 상자로 삽입 생성. 이는 범위를 갖지 않는 bbox 를 생성합니다.
# 따라서 절대 단위 (인치) 로 너비와 높이를 지정할 때만 의미가 있습니다.
axins2 = inset_axes(ax, width=0.5, height=0.4,
                    bbox_to_anchor=(0.33, 0.25),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
```
