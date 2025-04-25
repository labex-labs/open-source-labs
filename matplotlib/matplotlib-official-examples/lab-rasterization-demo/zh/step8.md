# 保存图形

我们将以 pdf 和 eps 格式保存图形。

```python
plt.savefig("test_rasterization.pdf", dpi=150)
plt.savefig("test_rasterization.eps", dpi=150)

if not plt.rcParams["text.usetex"]:
    plt.savefig("test_rasterization.svg", dpi=150)
    # svg 后端当前忽略 dpi
```
