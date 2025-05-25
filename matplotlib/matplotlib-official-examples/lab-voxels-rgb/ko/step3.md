# 구 생성

이제 플롯 중심에서 특정 거리 내에 있는 RGB 값에 대한 조건을 정의하여 플롯에 구를 생성합니다.

```python
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)

sphere = (rc - 0.5)**2 + (gc - 0.5)**2 + (bc - 0.5)**2 < 0.5**2
```
