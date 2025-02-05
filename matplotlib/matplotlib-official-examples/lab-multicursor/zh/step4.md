# 添加多光标

最后，我们将添加 `MultiCursor` 函数，以便在鼠标悬停在数据点上时在所有三个图上显示光标。

```python
multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```
