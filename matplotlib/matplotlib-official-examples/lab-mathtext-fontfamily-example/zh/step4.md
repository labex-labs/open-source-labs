# 设置标题的字体

我们还可以使用 `math_fontfamily` 参数来更改标题的字体族。

```python
ax.set_title(r"$数学模式下的标题：\ \int_{0}^{\infty } x^2 dx$",
             math_fontfamily='stixsans', size=14)
```
