# 创建绘图

现在，我们可以使用Matplotlib创建绘图。我们将使用`plot`函数来绘制数据，并使用`set_xlim`函数设置x轴的范围。

```python
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)  # decreasing time
ax.set_xlabel('decreasing time (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)

plt.show()
```
