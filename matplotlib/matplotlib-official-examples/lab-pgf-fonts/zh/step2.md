# 设置字体族

我们将使用 `font.family` 参数把字体族设置为“serif”（衬线字体）。此外，我们会将 `font.serif` 参数设置为空列表，以使用默认的 LaTeX 衬线字体。

```python
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": [],
})
```
