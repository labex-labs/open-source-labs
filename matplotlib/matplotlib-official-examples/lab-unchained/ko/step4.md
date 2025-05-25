# 한계 설정 및 눈금 제거

이 단계에서는 y 축 한계를 설정하고 플롯에서 눈금을 제거합니다.

```python
# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 70)

# No ticks
ax.set_xticks([])
ax.set_yticks([])
```
