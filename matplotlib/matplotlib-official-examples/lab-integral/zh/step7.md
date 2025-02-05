# 添加轴标签和刻度标签

使用 `figtext` 添加 x 轴和 y 轴标签。使用 `spines` 隐藏顶部和右侧的边框。使用 `set_xticks` 和 `set_yticks` 设置自定义刻度位置和标签。

```python
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])
```
