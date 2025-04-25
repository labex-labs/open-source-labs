# 双極子の電位を計算する

```python
def dipole_potential(x, y):
    """The electric dipole potential V, at position *x*, *y*."""
    r_sq = x**2 + y**2
    theta = np.arctan2(y, x)
    z = np.cos(theta)/r_sq
    return (np.max(z) - z) / (np.max(z) - np.min(z))

V = dipole_potential(x, y)
```

解説：

- `dipole_potential`は電気双極子の電位を計算する関数です。
- `V`は電気双極子の電位の配列です。
