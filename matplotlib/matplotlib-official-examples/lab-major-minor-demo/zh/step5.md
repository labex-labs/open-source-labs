# 主刻度和次刻度的自动刻度选择

```python
# 创建数据
t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

# 绘制数据
fig, ax = plt.subplots()
ax.plot(t, s)

# 设置次刻度定位器
ax.xaxis.set_minor_locator(AutoMinorLocator())

# 设置刻度参数
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# 显示绘图
plt.show()
```

在这一步中，我们创建新数据并进行绘制。然后我们设置次刻度定位器以自动选择次刻度的数量。之后，我们设置主刻度和次刻度的刻度参数，即刻度的宽度、长度及其颜色。最后，我们显示绘图。
