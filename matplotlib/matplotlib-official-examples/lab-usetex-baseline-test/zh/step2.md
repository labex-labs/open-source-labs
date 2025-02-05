# 设置Matplotlib字体

我们需要设置用于Matplotlib文本的字体。我们将使用Computer Modern字体，并将其设置为Matplotlib的默认字体。

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```
