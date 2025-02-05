# 绘制一个长宽比相等的圆

要设置相等的轴长宽比，我们可以使用 `axis('equal')` 函数。

```python
axs[0, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 1].axis('equal')
axs[0, 1].set_title('equal, looks like circle', fontsize=10)
```

生成的绘图将显示一个比例合适且视觉上吸引人的圆。
