# 임의 위치로 삽입 생성

`bbox_to_anchor` 매개변수를 사용하여 데이터 좌표에서 경계 상자를 지정하고, `bbox_transform` 매개변수를 사용하여 경계 상자에 대한 변환을 지정하여 임의 위치로 삽입을 생성할 수 있습니다.

```python
# ax.transData 를 변환으로 사용하여 데이터 좌표에서 삽입 생성
axins3 = inset_axes(ax2, width="100%", height="100%",
                    bbox_to_anchor=(1e-2, 2, 1e3, 3),
                    bbox_transform=ax2.transData, loc=2, borderpad=0)
```
