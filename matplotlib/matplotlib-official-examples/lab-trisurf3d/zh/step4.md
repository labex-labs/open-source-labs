# 将极坐标转换为笛卡尔坐标

我们将把极坐标转换为笛卡尔坐标：

```python
# 将极坐标（半径，角度）转换为笛卡尔坐标（x，y）。
# 在此阶段手动添加 (0, 0)，这样在 (x, y) 平面中就不会有重复的点。
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())
```
