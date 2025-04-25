# 设置 Matplotlib 字体

我们需要设置用于 Matplotlib 文本的字体。我们将使用 Computer Modern 字体，并将其设置为 Matplotlib 的默认字体。

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```
