# Creación de múltiples gráficos

También podemos crear múltiples gráficos en la misma figura.

```python
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Plot 1')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Plot 2')

plt.show()
```

Aquí, estamos usando la función `subplot` para crear dos gráficos uno al lado del otro en la misma figura. Pasamos tres argumentos a `subplot`: el número de filas, el número de columnas y el número del gráfico. Luego, creamos un gráfico en cada subgráfico.
