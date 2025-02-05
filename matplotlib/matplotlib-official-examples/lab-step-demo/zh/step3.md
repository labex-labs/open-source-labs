# 使用 `.step()` 进行绘图

我们可以使用 `.step()` 函数来创建分段常数曲线。`where` 参数决定了应该在何处绘制台阶。我们将使用不同的 `where` 值创建三个绘图。

```python
plt.step(x, y + 2, label='pre (default)', where='pre')
plt.step(x, y + 1, label='mid', where='mid')
plt.step(x, y, label='post', where='post')
plt.legend()
plt.show()
```

上述代码将创建一个包含三条分段常数曲线的绘图，每条曲线的 `where` 值都不同。
