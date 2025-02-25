# 渦巻きを作成する

```python
nverts = 50
npts = 100

# いくつかの渦巻きを作成する
r = np.arange(nverts)
theta = np.linspace(0, 2*np.pi, nverts)
xx = r * np.sin(theta)
yy = r * np.cos(theta)
spiral = np.column_stack([xx, yy])
```

次のステップは、Numpyを使って渦巻きを作成することです。渦巻きを作成するために、sinとcos関数を使用します。
