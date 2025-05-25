# 각 기본 3D 뷰 평면에 레이블 지정

2 단계에서 정의된 `annotate_axes` 함수를 사용하여 각 기본 3D 뷰 평면에 해당 각도로 레이블을 지정합니다.

```python
for plane, angles in views:
    label = f'{plane}\n{angles}'
    annotate_axes(axd[plane], label, fontsize=14)
```
