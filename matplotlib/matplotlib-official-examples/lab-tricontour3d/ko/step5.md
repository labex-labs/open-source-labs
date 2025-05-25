# 원치 않는 삼각형 마스크 처리

x 및 y 좌표의 평균을 사용하여 원치 않는 삼각형을 마스크 처리합니다.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
