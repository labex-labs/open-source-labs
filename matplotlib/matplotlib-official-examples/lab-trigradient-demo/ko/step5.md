# 전기장 계산

```python
tci = CubicTriInterpolator(triang, -V)

(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
```

설명:

- `CubicTriInterpolator`는 3 차 다항식을 사용하여 데이터를 보간하는 클래스입니다.
- `tci`는 `CubicTriInterpolator` 클래스의 인스턴스입니다.
- `(Ex, Ey)`는 전기장입니다.
- `E_norm`은 정규화된 전기장입니다.
