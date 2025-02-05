# 添加水平网格线

最后，我们将使用 `yaxis.grid()` 函数为箱线图添加水平网格线。

```python
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Three Separate Samples')
    ax.set_ylabel('Observed Values')

plt.show()
```
