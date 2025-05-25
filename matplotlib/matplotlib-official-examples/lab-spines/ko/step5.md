# 하단 및 왼쪽 측면에 대한 스파인 (Spine) 사용자 정의

두 번째 서브플롯에서는 플롯의 하단 및 왼쪽 측면에만 스파인을 표시합니다. `set_visible` 메서드를 사용하여 플롯의 오른쪽 및 상단 측면에 있는 스파인을 숨길 수 있습니다.

```python
ax1.plot(x, y)
ax1.set_title('Bottom-Left Spines')

# Hide the right and top spines
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
```
