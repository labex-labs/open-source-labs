# 축 조정 및 Y-Label 을 위한 공간 확보

이 단계에서는 `add_auto_adjustable_area` 메서드를 사용하여 축을 조정하고 y-label 을 위한 공간을 확보합니다. 또한 두 번째 축에 대한 제목과 x-label 을 설정합니다.

```python
divider.add_auto_adjustable_area(use_axes=[ax1], pad=0.1,
                                 adjust_dirs=["left"])
divider.add_auto_adjustable_area(use_axes=[ax2], pad=0.1,
                                 adjust_dirs=["right"])
divider.add_auto_adjustable_area(use_axes=[ax1, ax2], pad=0.1,
                                 adjust_dirs=["top", "bottom"])

ax1.set_yticks([0.5], labels=["very long label"])
ax2.set_title("Title")
ax2.set_xlabel("X - Label")
```
