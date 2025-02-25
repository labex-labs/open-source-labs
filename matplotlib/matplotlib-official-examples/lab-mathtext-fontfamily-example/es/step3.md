# Establecer texto en la gráfica

A continuación, estableceremos el texto en la gráfica utilizando la función `text()`. Utilizaremos el parámetro `math_fontfamily` para cambiar la familia de fuentes para cada elemento de texto individual.

```python
# Un texto que mezcla texto normal y texto matemático.
msg = (r"Texto normal. $Texto\ en\ modo\ matemático:\ "
       r"\int_{0}^{\infty } x^2 dx$")

# Establece el texto en la gráfica.
ax.text(1, 7, msg, size=12, math_fontfamily='cm')

# Establece otra fuente para el siguiente texto.
ax.text(1, 3, msg, size=12, math_fontfamily='dejavuserif')
```
