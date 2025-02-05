# 使用 `.plot()` 进行绘图

通过使用 `.plot()` 函数的 `drawstyle` 参数，我们可以实现与 `.step()` 相同的效果。我们将使用不同的 `drawstyle` 值创建三个绘图。

```python
plt.plot(x, y + 2, drawstyle='steps', label='steps (=steps-pre)')
plt.plot(x, y + 1, drawstyle='steps-mid', label='steps-mid')
plt.plot(x, y, drawstyle='steps-post', label='steps-post')
plt.legend()
plt.show()
```

上述代码将创建一个包含三条分段常数曲线的绘图，每条曲线的 `drawstyle` 值都不同。
