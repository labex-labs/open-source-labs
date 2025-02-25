# Formateando el estilo del gráfico

A continuación, personalicemos el estilo de nuestro gráfico. Podemos utilizar el tercer argumento opcional de la función `plot` para especificar la cadena de formato, que indica el color y el tipo de línea del gráfico. Por ejemplo, grafiquemos la misma gráfica de líneas con círculos rojos:

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
```

Explicación:

- Utilizamos la cadena de formato `'ro'` para indicar círculos rojos para el gráfico.
- La función `axis` se utiliza para establecer la ventana de visualización de los ejes, especificando el rango de valores para los ejes x e y.
