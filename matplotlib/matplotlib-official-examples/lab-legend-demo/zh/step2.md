# 绘制更复杂的标签

在这一步中，我们将绘制更复杂的标签。

```python
# 定义图表数据
x = np.linspace(0, 1)

# 创建一个包含多条线的图表
fig, (ax0, ax1) = plt.subplots(2, 1)
for n in range(1, 5):
    ax0.plot(x, x**n, label=f"{n=}")

# 创建一个具有多列和标题的图例
leg = ax0.legend(loc="upper left", bbox_to_anchor=[0, 1],
                 ncols=2, shadow=True, title="Legend", fancybox=True)
leg.get_title().set_color("red")

# 创建一个包含多条线和标记的图表
ax1.plot(x, x**2, label="multi\nline")
half_pi = np.linspace(0, np.pi / 2)
ax1.plot(np.sin(half_pi), np.cos(half_pi), label=r"$\frac{1}{2}\pi$")
ax1.plot(x, 2**(x**2), label="$2^{x^2}$")

# 创建一个带有阴影的图例
ax1.legend(shadow=True, fancybox=True)

# 显示图表
plt.show()
```
