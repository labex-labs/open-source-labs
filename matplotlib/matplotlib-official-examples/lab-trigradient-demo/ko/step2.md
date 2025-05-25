# 쌍극자의 전기적 전위 계산

```python
def dipole_potential(x, y):
    """The electric dipole potential V, at position *x*, *y*."""
    r_sq = x**2 + y**2
    theta = np.arctan2(y, x)
    z = np.cos(theta)/r_sq
    return (np.max(z) - z) / (np.max(z) - np.min(z))

V = dipole_potential(x, y)
```

설명:

- `dipole_potential`은 전기 쌍극자 전위를 계산하는 함수입니다.
- `V`는 전기 쌍극자 전위의 배열입니다.
