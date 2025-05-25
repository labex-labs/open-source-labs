# 데이터 범위로 제한된 경계 (Bounds) 를 가진 스파인 (Spine) 사용자 정의

세 번째 서브플롯에서는 데이터 범위로 제한된 경계를 가진 스파인을 표시합니다. `set_bounds` 메서드를 사용하여 각 스파인의 범위를 데이터 범위로 제한할 수 있습니다.

```python
ax2.plot(x, y)
ax2.set_title('Spines with Bounds Limited to Data Range')

# Only draw spines for the data range, not in the margins
ax2.spines.bottom.set_bounds(x.min(), x.max())
ax2.spines.left.set_bounds(y.min(), y.max())
# Hide the right and top spines
ax2.spines.right.set_visible(False)
ax2.spines.top.set_visible(False)
```
