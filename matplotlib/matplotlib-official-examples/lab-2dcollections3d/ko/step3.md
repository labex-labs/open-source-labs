# 3D 플롯에 2D 데이터 플롯

세 번째 단계는 `ax.plot`과 `ax.scatter`를 사용하여 3D 플롯에 2D 데이터를 플롯하는 것입니다. `ax.plot` 함수는 x 축과 y 축을 사용하여 사인 곡선을 플롯합니다. `ax.scatter` 함수는 x 축과 z 축에 산점도 데이터를 플롯합니다.

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
