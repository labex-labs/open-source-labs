# 计算偶极子的电势

```python
def dipole_potential(x, y):
    """The electric dipole potential V, at position *x*, *y*."""
    r_sq = x**2 + y**2
    theta = np.arctan2(y, x)
    z = np.cos(theta)/r_sq
    return (np.max(z) - z) / (np.max(z) - np.min(z))

V = dipole_potential(x, y)
```

解释：

- `dipole_potential` 是一个计算电偶极子电势的函数。
- `V` 是电偶极子电势的数组。
