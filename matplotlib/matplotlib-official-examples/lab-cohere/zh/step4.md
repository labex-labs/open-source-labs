# 绘制相干性

现在我们可以使用 Matplotlib 的 `cohere` 函数来绘制这两个信号的相干性。

```python
cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Coherence')
```
