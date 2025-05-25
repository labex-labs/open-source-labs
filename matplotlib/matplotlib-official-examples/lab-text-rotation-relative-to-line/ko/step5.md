# 올바른 회전으로 텍스트 플롯

마지막으로, 선의 회전을 고려하여 지정된 위치에 텍스트를 플롯합니다. 이렇게 하면 텍스트가 선에 상대적으로 올바른 각도로 회전하게 됩니다.

```python
# Plot text
th2 = ax.text(*l2, 'text rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor',
              transform_rotates_text=True)
```
