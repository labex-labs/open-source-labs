# 动态绘制图形

第五步是动态绘制图形。我们将使用一个 for 循环来遍历一系列 phi 值。在每次迭代中，我们将移除上一个线条集合，生成新的数据，绘制新的线框，并在继续之前短暂暂停。

```python
wframe = None
tstart = time.time()
for phi in np.linspace(0, 180. / np.pi, 100):
    if wframe:
        wframe.remove()
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    plt.pause(.001)
```
