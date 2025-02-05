# 为等轴长宽比自动调整数据范围

我们还可以使用 `set_aspect('equal', 'box')` 函数为等轴长宽比自动调整数据范围。

```python
axs[1, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 1].set_aspect('equal', 'box')
axs[1, 1].set_title('still a circle, auto-adjusted data limits', fontsize=10)
```

生成的绘图将显示一个仍然比例合适且视觉上吸引人的圆。
