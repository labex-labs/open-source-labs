# Y2 축 생성

마지막으로, 오프셋 (20, 0) 을 사용하여 플롯의 오른쪽에 새로운 y2 축을 생성하고 레이블을 지정합니다.

```python
ax.axis["right2"] = ax.new_fixed_axis(loc="right", offset=(20, 0))
ax.axis["right2"].label.set_text("Label Y2")
```
