# Guardar el gráfico

Una vez que hemos creado un gráfico, podemos guardarlo en un archivo.

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.savefig('my_plot.png')
```

Aquí, estamos usando la función `savefig` para guardar nuestro gráfico en un archivo llamado `my_plot.png`.
