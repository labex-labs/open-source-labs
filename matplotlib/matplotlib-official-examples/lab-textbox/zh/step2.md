# 创建初始绘图

接下来，我们创建一个初始绘图，该绘图将根据用户输入进行更新。在这个例子中，我们创建一个以`t`为自变量的函数的绘图。

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-2.0, 2.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)
```
