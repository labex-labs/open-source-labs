# 创建球体

现在，我们将通过定义一个条件来在图表中创建一个球体，该条件针对的是与图表中心距离在一定范围内的 RGB 值。

```python
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)

sphere = (rc - 0.5)**2 + (gc - 0.5)**2 + (bc - 0.5)**2 < 0.5**2
```
