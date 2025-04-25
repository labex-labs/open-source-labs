# 在示例 y = x 图上比较“symlog”和“asinh”的行为

我们将在示例 y = x 图上比较“symlog”和“asinh”的行为。我们将把同一个图绘制两次，一次使用“symlog”，另一次使用“asinh”。

```python
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex=True)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')
```
