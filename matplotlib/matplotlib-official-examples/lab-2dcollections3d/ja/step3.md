# 3D プロットに 2D データをプロットする

3 番目のステップは、`ax.plot` と `ax.scatter` を使用して 3D プロットに 2D データをプロットすることです。`ax.plot` 関数は、x 軸と y 軸を使用してサインカーブをプロットします。`ax.scatter` 関数は、x 軸と z 軸に散布図データをプロットします。

```python
# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

# Plot scatterplot data (20 2D points per colour) on the x and z axes.
colors = ('r', 'g', 'b', 'k')

# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)
# By using zdir='y', the y value of these points is fixed to the zs value 0
# and the (x, y) points are plotted on the x and z axes.
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x, z)')
```
