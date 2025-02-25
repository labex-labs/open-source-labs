# Меняем ориентацию графика

В этом шаге мы изменим ориентацию графика с использованием параметра `orientation`. Мы установим ориентацию в `'x'`, чтобы стебели были проектированы вдоль оси x, а базовая линия находилась в плоскости yz.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()
```
