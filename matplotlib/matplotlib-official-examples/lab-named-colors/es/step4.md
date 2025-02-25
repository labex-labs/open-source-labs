# Creando un gráfico de dispersión

También podemos utilizar Matplotlib para crear un gráfico de dispersión. En este ejemplo, crearemos un gráfico de dispersión que muestre la relación entre los valores de x e y.

```python
import matplotlib.pyplot as plt

# valores del eje x
x = [1, 2, 3, 4, 5]

# valores del eje y
y = [2, 4, 6, 8, 10]

# graficando los puntos
plt.scatter(x, y)

# estableciendo el título
plt.title("Gráfico de dispersión simple")

# estableciendo la etiqueta del eje x
plt.xlabel("Eje x")

# estableciendo la etiqueta del eje y
plt.ylabel("Eje y")

# mostrando el gráfico
plt.show()
```
