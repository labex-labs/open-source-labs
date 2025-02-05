# 生成数据

在这一步中，我们使用 numpy 生成随机数据点。

```python
# 为保证可重复性而固定随机状态
np.random.seed(19680801)

# 生成随机数据点
x, y = 4*(np.random.rand(2, 100) -.5)
```
