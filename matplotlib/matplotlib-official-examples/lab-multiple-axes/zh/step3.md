# 绘制圆和初始点

第三步是在左边的子图上绘制圆和初始点。我们创建一个角度数组来生成圆，然后绘制每个角度的正弦值和余弦值。我们还在原点处绘制一个点。

```python
x = np.linspace(0, 2 * np.pi, 50)
axl.plot(np.cos(x), np.sin(x), "k", lw=0.3)
point, = axl.plot(0, 0, "o")
```
