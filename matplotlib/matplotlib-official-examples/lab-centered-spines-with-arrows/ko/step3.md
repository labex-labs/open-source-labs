# 축 (spines) 이동

기본적으로 축 (spines) 은 플롯의 가장자리에 그려집니다. 이 경우, 왼쪽 및 하단 축을 플롯의 중심으로 이동하려고 합니다.

```python
ax.spines[["left", "bottom"]].set_position(("data", 0))
```
