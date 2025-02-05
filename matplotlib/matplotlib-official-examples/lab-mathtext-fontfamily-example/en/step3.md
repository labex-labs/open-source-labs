# Set Text in the Plot

Next, we will set the text in the plot using the `text()` function. We will use the `math_fontfamily` parameter to change the font family for each individual text element.

```python
# A text mixing normal text and math text.
msg = (r"Normal Text. $Text\ in\ math\ mode:\ "
       r"\int_{0}^{\infty } x^2 dx$")

# Set the text in the plot.
ax.text(1, 7, msg, size=12, math_fontfamily='cm')

# Set another font for the next text.
ax.text(1, 3, msg, size=12, math_fontfamily='dejavuserif')
```
