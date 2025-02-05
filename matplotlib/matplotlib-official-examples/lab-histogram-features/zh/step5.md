# 自定义直方图

在这一步中，我们将通过添加标签、标题和调整布局来自定义直方图。

```python
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()
```
