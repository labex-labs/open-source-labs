# Creando un gráfico circular

También podemos utilizar Matplotlib para crear un gráfico circular. En este ejemplo, crearemos un gráfico circular que muestre el porcentaje de personas que prefieren diferentes tipos de pizza.

```python
import matplotlib.pyplot as plt

# datos para graficar
sizes = [30, 40, 10, 20]
labels = ["Pepperoni", "Champiñón", "Cebolla", "Salchichón"]

# creando el gráfico circular
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# estableciendo el título
plt.title("Gráfico circular simple")

# mostrando el gráfico
plt.show()
```
