# 设置绘图的范围和标签

最后，我们使用 `set` 函数来设置绘图的范围和标签。

```python
ax.set(xlim=(0, 10), ylim=(1, 9), zlim=(0, 0.35),
       xlabel='x', ylabel=r'$\lambda$', zlabel='probability')
```
