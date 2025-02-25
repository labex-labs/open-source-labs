# Creando un gráfico simple

Ahora que hemos importado Matplotlib, podemos utilizarlo para crear un gráfico simple. En este ejemplo, crearemos un gráfico de línea que muestre la relación entre los valores de x e y.

```python
import matplotlib.pyplot as plt

# valores del eje x
x = [1, 2, 3, 4, 5]

# valores del eje y
y = [2, 4, 6, 8, 10]

# trazar la línea
plt.plot(x, y)

# establecer el título
plt.title("Gráfico de línea simple")

# establecer la etiqueta del eje x
plt.xlabel("Eje x")

# establecer la etiqueta del eje y
plt.ylabel("Eje y")

# mostrar el gráfico
plt.show()
```
