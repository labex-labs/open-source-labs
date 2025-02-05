# 在保持轴长宽比相等的同时调整绘图范围

我们还可以在保持轴长宽比相等的情况下调整绘图范围。

```python
axs[1, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 0].axis('equal')
axs[1, 0].set(xlim=(-3, 3), ylim=(-3, 3))
axs[1, 0].set_title('still a circle, even after changing limits', fontsize=10)
```

生成的绘图将显示一个即使在我们更改范围后仍然保持比例的圆。
