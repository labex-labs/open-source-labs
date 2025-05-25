# Definir o Texto no Gráfico

Em seguida, definiremos o texto no gráfico usando a função `text()`. Usaremos o parâmetro `math_fontfamily` para alterar a família de fontes para cada elemento de texto individual.

```python
# A text mixing normal text and math text.
msg = (r"Normal Text. $Text\ in\ math\ mode:\ "
       r"\int_{0}^{\infty } x^2 dx$")

# Set the text in the plot.
ax.text(1, 7, msg, size=12, math_fontfamily='cm')

# Set another font for the next text.
ax.text(1, 3, msg, size=12, math_fontfamily='dejavuserif')
```
