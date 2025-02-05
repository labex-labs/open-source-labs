# 在图表中设置文本

接下来，我们将使用 `text()` 函数在图表中设置文本。我们将使用 `math_fontfamily` 参数为每个单独的文本元素更改字体族。

```python
# 一段混合了普通文本和数学文本的内容。
msg = (r"正常文本。$数学模式下的文本：\ "
       r"\int_{0}^{\infty } x^2 dx$")

# 在图表中设置文本。
ax.text(1, 7, msg, size=12, math_fontfamily='cm')

# 为下一段文本设置另一种字体。
ax.text(1, 3, msg, size=12, math_fontfamily='dejavuserif')
```
