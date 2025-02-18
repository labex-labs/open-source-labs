# Personalización del gráfico

Ahora que tenemos un gráfico básico, personalicémoslo.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='red', marker='o')
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.show()
```

Aquí, hemos agregado algunas personalizaciones a nuestro gráfico. Hemos cambiado el color de la línea a rojo y agregado marcadores circulares a cada punto de datos. También hemos agregado un título y etiquetas de eje a nuestro gráfico.
