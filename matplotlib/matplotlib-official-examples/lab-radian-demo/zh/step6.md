# 添加标签并调整布局

使用 matplotlib.pyplot 中的 title、xlabel 和 ylabel 函数为子图添加标题和轴标签。使用 tight_layout 函数调整子图的布局。

```python
axs[0].set_title('Cosine with Radian X-Axis')
axs[0].set_xlabel('Radians')
axs[0].set_ylabel('Cosine')
axs[1].set_title('Cosine with Degree X-Axis')
axs[1].set_xlabel('Degrees')
axs[1].set_ylabel('Cosine')
fig.tight_layout()
```
