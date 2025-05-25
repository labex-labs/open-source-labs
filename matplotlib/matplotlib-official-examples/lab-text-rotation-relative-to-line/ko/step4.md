# 올바른 회전 없이 텍스트 플롯

이제 선의 회전을 고려하지 않고 지정된 위치에 텍스트를 플롯합니다. 이렇게 하면 텍스트가 45 도 각도로 회전하게 되는데, 이는 우리가 원하는 바가 아닙니다.

```python
# Plot text
th1 = ax.text(*l1, 'text not rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor')
```
