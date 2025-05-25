# 줌 및 각도 뷰 설정

`view_init` 및 `set_box_aspect` 메서드를 사용하여 줌 및 각도 뷰를 설정합니다. X 방향으로 40 도, Y 방향으로 -30 도의 각도 뷰를 설정하고 줌을 0.9 로 설정합니다.

```python
# Set zoom and angle view
ax.view_init(40, -30, 0)
ax.set_box_aspect(None, zoom=0.9)
```
