# 生成一个填充多边形

现在，我们可以使用 `fill()` 函数生成一个填充多边形。我们将使用科赫雪花函数来生成多边形的坐标。

```python
x, y = koch_snowflake(order=5)

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.fill(x, y)
plt.show()
```
