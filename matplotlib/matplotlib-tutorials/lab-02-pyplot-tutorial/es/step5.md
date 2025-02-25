# Personalizando propiedades de líneas

Matplotlib te permite personalizar varias propiedades de líneas, como el ancho de línea, el estilo de trazos discontinúos y el color. Veamos algunos métodos para establecer propiedades de líneas:

```python
x = np.arange(0, 5, 0.1)
line, = plt.plot(x, np.sin(x), '-')

# Utilizando el método setter de la instancia Line2D
line.set_linewidth(2.0)  # Establece la propiedad de ancho de línea de la línea en 2.0

# Utilizando la función setp de pyplot
plt.setp(line, color='r', linewidth=2.0)  # Establece las propiedades de color y ancho de línea utilizando la función setp

plt.show()
```

Explicación:

- Creamos un array `x` y calculamos los valores correspondientes de y utilizando la función `np.sin`.
- Se llama a la función `plot` para crear un gráfico de líneas.
- Utilizamos el método `set` de la instancia `Line2D` para establecer la propiedad de ancho de línea de la línea en 2.0.
- Alternativamente, podemos utilizar la función `setp` para establecer múltiples propiedades de la línea, como el color y el ancho de línea, utilizando argumentos de palabras clave.
