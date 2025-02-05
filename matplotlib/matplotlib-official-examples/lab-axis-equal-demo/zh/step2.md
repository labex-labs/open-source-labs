# 绘制一个长宽比不等的圆

我们将首先绘制一个长宽比不等的圆，以说明设置相等长宽比的重要性。

```python
an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('not equal, looks like ellipse', fontsize=10)
```

生成的绘图将显示一个由于长宽比不等而看起来拉长的圆。
