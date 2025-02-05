# 设置第二个y轴的刻度标签

我们可以使用`set_xticks`函数来设置第二个y轴的刻度标签，并将刻度位置和标签作为参数传入。

```python
ax2.set_xticks([0.,.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
               labels=["$0$", r"$\frac{1}{2}\pi$",
                       r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
```
