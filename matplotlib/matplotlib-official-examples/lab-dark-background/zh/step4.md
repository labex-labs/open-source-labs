# 绘制数据

在这一步中，我们将绘制上一步中生成的示例数据。我们将使用一个 `for` 循环来绘制多个具有不同相位的正弦波。

```python
fig, ax = plt.subplots()

ncolors = len(plt.rcParams['axes.prop_cycle'])
shift = np.linspace(0, L, ncolors, endpoint=False)

for s in shift:
    # 绘制相位偏移为 s 的正弦波
    ax.plot(x, np.sin(x + s), 'o-')

ax.set_xlabel('x 轴')
ax.set_ylabel('y 轴')
ax.set_title("'dark_background' 样式表")

plt.show()
```
